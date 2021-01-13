#!/usr/bin/python
# coding=utf-8
"""
Parse my bibtex file and create jekyll-friendly collection entries.
"""
import argparse
import os
import sys
from functools import cmp_to_key
from pybtex.database.input import bibtex

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('bibtex_file', action='store', type=str,
        help='Path to input bibtex file.')
    parser.add_argument('output_folder', action='store', type=str,
        help='Output folder')
    return parser.parse_args()


def html_escape(text):
    """Produce entities within text."""
    # Check latex special characters: https://en.wikibooks.org/wiki/LaTeX/Special_Characters#Escaped_codes
    # HTML entitites: https://dev.w3.org/html5/html-author/charref
    escape_entities = [
        ('&', '&amp;'),
        # Tilde
        ('\\~{a}', '&atilde;'), ('{\\~a}', '&atilde;'),
        ('\\~{A}', '&Atilde;'), ('{\\~A}', '&Atilde;'),
        ('\\~{n}', '&ntilde;'), ('{\\~n}', '&ntilde;'),
        ('\\~{N}', '&Ntilde;'), ('{\\~N}', '&Ntilde;'),
        ('\\~{o}', '&otilde;'), ('{\\~o}', '&otilde;'),
        ('\\~{O}', '&Otilde;'), ('{\\~O}', '&Otilde;'),
        ('\\~{i}', '&itilde;'), ('{\\~i}', '&itilde;'),
        ('\\~{I}', '&Itilde;'), ('{\\~I}', '&Itilde;'),
        ('\\~{u}', '&utilde;'), ('{\\~u}', '&utilde;'),
        ('\\~{U}', '&Utilde;'), ('{\\~U}', '&Utilde;'),
        # Carons
        ('\\v{c}', '&ccaron;'), ('{\\v c}', '&ccaron;'),
        ('\\v{C}', '&Ccaron;'), ('{\\v C}', '&Ccaron;'),
        ('\\v{d}', '&dcaron;'), ('{\\v d}', '&dcaron;'),
        ('\\v{D}', '&Dcaron;'), ('{\\v D}', '&Dcaron;'),
        ('\\v{e}', '&ecaron;'), ('{\\v e}', '&ecaron;'),
        ('\\v{E}', '&Ecaron;'), ('{\\v E}', '&Ecaron;'),
        ('\\v{l}', '&lcaron;'), ('{\\v l}', '&lcaron;'),
        ('\\v{L}', '&Lcaron;'), ('{\\v L}', '&Lcaron;'),
        ('\\v{n}', '&ncaron;'), ('{\\v n}', '&ncaron;'),
        ('\\v{N}', '&Ncaron;'), ('{\\v N}', '&Ncaron;'),
        ('\\v{r}', '&rcaron;'), ('{\\v r}', '&rcaron;'),
        ('\\v{R}', '&Rcaron;'), ('{\\v R}', '&Rcaron;'),
        ('\\v{s}', '&scaron;'), ('{\\v s}', '&scaron;'),
        ('\\v{S}', '&Scaron;'), ('{\\v S}', '&Scaron;'),
        ('\\v{t}', '&tcaron;'), ('{\\v t}', '&tcaron;'),
        ('\\v{T}', '&Tcaron;'), ('{\\v T}', '&Tcaron;'),
        ('\\v{z}', '&zcaron;'), ('{\\v z}', '&zcaron;'),
        ('\\v{Z}', '&Zcaron;'), ('{\\v Z}', '&Zcaron;'),
        # Acute accents
        ("\\'{a}", '&aacute;'), ("{\\' a}", '&aacute;'), ("{\\'a}", '&aacute;'),
        ("\\'{A}", '&Aacute;'), ("{\\' A}", '&Aacute;'), ("{\\'A}", '&Aacute;'),
        ("\\'{e}", '&eacute;'), ("{\\' e}", '&eacute;'), ("{\\'e}", '&eacute;'),
        ("\\'{E}", '&Eacute;'), ("{\\' E}", '&Eacute;'), ("{\\'E}", '&Eacute;'),
        ("\\'{i}", '&iacute;'), ("{\\' i}", '&iacute;'), ("{\\'i}", '&iacute;'),
        ("\\'{I}", '&Iacute;'), ("{\\' I}", '&Iacute;'), ("{\\'I}", '&Iacute;'),
        ("\\'{o}", '&oacute;'), ("{\\' o}", '&oacute;'), ("{\\'o}", '&oacute;'),
        ("\\'{O}", '&Oacute;'), ("{\\' O}", '&Oacute;'), ("{\\'O}", '&Oacute;'),
        ("\\'{u}", '&uacute;'), ("{\\' u}", '&uacute;'), ("{\\'u}", '&uacute;'),
        ("\\'{U}", '&Uacute;'), ("{\\' U}", '&Uacute;'), ("{\\'U}", '&Uacute;'),
        ("\\'{c}", '&cacute;'), ("{\\' c}", '&cacute;'), ("{\\'c}", '&cacute;'),
        ("\\'{C}", '&Cacute;'), ("{\\' C}", '&Cacute;'), ("{\\'C}", '&Cacute;'),
        ("\\'{l}", '&lacute;'), ("{\\' l}", '&lacute;'), ("{\\'l}", '&lacute;'),
        ("\\'{L}", '&Lacute;'), ("{\\' L}", '&Lacute;'), ("{\\'L}", '&Lacute;'),
        # N("\\'{a}", '&aacute;'), ("{\\' a}", '&aacute;'), ("{\\'a}", '&aacute;'),
        # ("\\'{A}", '&Aacute;'), ("{\\' A}", '&Aacute;'), ("{\\'A}", '&Aacute;'),
        # R("\\'{a}", '&aacute;'), ("{\\' a}", '&aacute;'), ("{\\'a}", '&aacute;'),
        # ("\\'{A}", '&Aacute;'), ("{\\' A}", '&Aacute;'), ("{\\'A}", '&Aacute;'),
        # S("\\'{a}", '&aacute;'), ("{\\' a}", '&aacute;'), ("{\\'a}", '&aacute;'),
        # ("\\'{A}", '&Aacute;'), ("{\\' A}", '&Aacute;'), ("{\\'A}", '&Aacute;'),
        # Cedilla
        ('\\c{c}', '&ccedil;'), ('\\c{C}', '&Ccedil;'),
        ('\\c{g}', '&gcedil;'), ('\\c{G}', '&Gcedil;'),
        ('\\c{k}', '&kcedil;'), ('\\c{K}', '&Kcedil;'),
        ('\\c{l}', '&lcedil;'), ('\\c{L}', '&Lcedil;'),
        ('\\c{n}', '&ncedil;'), ('\\c{N}', '&Ncedil;'),
        ('\\c{r}', '&rcedil;'), ('\\c{R}', '&Rcedil;'),
        ('\\c{s}', '&scedil;'), ('\\c{S}', '&Scedil;'),
        ('\\c{t}', '&tcedil;'), ('\\c{T}', '&Tcedil;'),
        # Breve
        ('\\u{a}', '&abreve;'), ('\\u{A}', '&Abreve;'),
        ('\\u{g}', '&gbreve;'), ('\\u{G}', '&Gbreve;'),
        ('\\u{u}', '&ubreve;'), ('\\u{U}', '&Ubreve;'),
        # Grave accents
        ('\\`{a}', '&agrave;'), ('{\\` a}', '&agrave;'), ('{\\`a}', '&agrave;'),
        ('\\`{A}', '&Agrave;'), ('{\\` A}', '&Agrave;'), ('{\\`A}', '&Agrave;'),
        ('\\`{e}', '&egrave;'), ('{\\` e}', '&egrave;'), ('{\\`e}', '&egrave;'),
        ('\\`{E}', '&Egrave;'), ('{\\` E}', '&Egrave;'), ('{\\`E}', '&Egrave;'),
        ('\\`{i}', '&igrave;'), ('{\\` i}', '&igrave;'), ('{\\`i}', '&igrave;'),
        ('\\`{I}', '&Igrave;'), ('{\\` I}', '&Igrave;'), ('{\\`I}', '&Igrave;'),
        ('\\`{o}', '&ograve;'), ('{\\` o}', '&ograve;'), ('{\\`o}', '&ograve;'),
        ('\\`{O}', '&Ograve;'), ('{\\` O}', '&Ograve;'), ('{\\`O}', '&Ograve;'),
        ('\\`{u}', '&ugrave;'), ('{\\` u}', '&ugrave;'), ('{\\`u}', '&ugrave;'),
        ('\\`{U}', '&Ugrave;'), ('{\\` U}', '&Ugrave;'), ('{\\`U}', '&Ugrave;'),
        # German umlauts
        ('\\"{a}', '&auml;'), ('{\\" a}', '&auml;'), ('{\\"a}', '&auml;'), ('ä', '&auml;'),
        ('\\"{A}', '&Auml;'), ('{\\" A}', '&Auml;'), ('{\\"A}', '&Auml;'), ('Ä', '&Auml;'),
        ('\\"{o}', '&ouml;'), ('{\\" o}', '&ouml;'), ('{\\"o}', '&ouml;'), ('ö', '&ouml;'),
        ('\\"{O}', '&Ouml;'), ('{\\" O}', '&Ouml;'), ('{\\"O}', '&Ouml;'), ('Ö', '&Ouml;'),
        ('\\"{u}', '&uuml;'), ('{\\" u}', '&uuml;'), ('{\\"u}', '&uuml;'), ('ü', '&uuml;'),
        ('\\"{U}', '&Uuml;'), ('{\\" U}', '&Uuml;'), ('{\\"U}', '&Uuml;'), ('Ü', '&Uuml;'),
        ('ß', '&szlig;'),
        # Quotation marks and apostrophes
        ("'", "&apos;"), ('"', '&quot;'),
        # Finally, strip parentheses and unused commands
        ('\\emph', ''), ('\\textbf', ''),
        ('et al.', '<i>et al.</i>'),
        ('{', ''), ('}', ''),
        ('--', '&ndash;')
    ]   
    for search, repl in escape_entities:
        text = text.replace(search, repl)
    return text
    # html_escape_table = {
    #     "&": "&amp;",
    #     '"': "&quot;",
    #     "'": "&apos;"
    #     }
    # return "".join(html_escape_table.get(c,c) for c in text)


def author_name(p):
    """Output the pybtex.Person's name"""
    def abbrev_first_name(fn):
        return fn[:1] + '.'

    tokens = [abbrev_first_name(fn) for fn in p.first_names] + p.middle_names + p.prelast_names + p.last_names
    return ' '.join(tokens)


def extract_authors(persons, max_num):
    names = [author_name(p) for p in persons]
    if max_num is None or len(names) <= max_num:
        return ', '.join(names)
    else:
        return ', '.join(names[:max_num] + ['et al.'])
    

def dump_markdown(output_folder, entry):
    # print(entry.__dict__)
    # print(entry.type)
    year = int(entry.fields['year'])
    key = entry.key
    rank = pub_rank(entry)
    filename = os.path.join(output_folder, f'{year}-{rank:02d}-{key}.md')
    title = html_escape(entry.fields["title"].replace("{", "").replace("}","").replace("\\",""))

    if 'max_author_display' in entry.fields:
        max_author_display = int(entry.fields['max_author_display'])
    else:
        max_author_display = None
    authors = html_escape(extract_authors(entry.persons['author'], max_author_display))

    md = f'---\ntitle: "{title}"\n'
    # md += f'collection: theses\n'

            #md += """\npermalink: """ + publist[pubsource]["collection"]["permalink"]  + html_filename
            
            # note = False
            # if "note" in b.keys():
            #     if len(str(b["note"])) > 5:
            #         md += "\nexcerpt: '" + html_escape(b["note"]) + "'"
            #         note = True

    md += f'year: {year}\n'
    md += f'authors: "{authors}"\n'
    venue_extra = None
    if entry.type in ['phdthesis', 'mscthesis', 'bscthesis']:
        thesis_type = {
            'phdthesis': 'PhD thesis',
            'mscthesis': "Master's thesis",
            'bscthesis': "Bachelor's thesis"
        }
        md += f'thesis_type: "{thesis_type[entry.type]}"\n'
        venue = entry.fields['school']
    elif entry.type in ['inproceedings']:
        venue = 'In ' + entry.fields['booktitle']
    elif entry.type in ['article']:
        venue = entry.fields['journal']
        if 'volume' in entry.fields:
            venue_extra = entry.fields['volume']
            num = None
            if 'number' in entry.fields:
                num = entry.fields['number']
            if 'issue' in entry.fields:
                num = entry.fields['issue']
            if num is not None:
                venue_extra += f'({num})'
            
            if 'pages' in entry.fields:
                venue_extra += ':' + entry.fields['pages']

    venue = html_escape(venue)
    venue_extra = None if venue_extra is None else html_escape(venue_extra)
    md += f'venue: "{venue}"\n'
    
    # Add download/further links
    if 'venue_url' in entry.fields:
        md += f'venue_url: {entry.fields["venue_url"]}\n'
    if 'venue_abbreviation' in entry.fields:
        md += f'venue_abbrev: {entry.fields["venue_abbreviation"]}\n'
    if venue_extra is not None:
        md += f'venue_extra: "{venue_extra}"\n'
    # Author/open access pdf
    if 'pdf_url' in entry.fields:
        md += f'pdf_url: {entry.fields["pdf_url"]}\n'
    if 'arxiv_url' in entry.fields:
        md += f'arxiv_url: {entry.fields["arxiv_url"]}\n'
    # Official paper
    if 'doi_url' in entry.fields:
        md += f'doi_url: {entry.fields["doi_url"]}\n'
    if 'publisher_url' in entry.fields:
        md += f'publisher_url: {entry.fields["publisher_url"]}\n'
    # Supplemental material
    if 'supplemental_url' in entry.fields:
        md += f'supplemental_url: {entry.fields["supplemental_url"]}\n'
    # Slide deck
    if 'slide_url' in entry.fields:
        md += f'slide_url: {entry.fields["slide_url"]}\n'
    # Video
    if 'video_url' in entry.fields:
        md += f'video_url: {entry.fields["video_url"]}\n'
    # Data(set) download
    if 'data_url' in entry.fields:
        md += f'data_url: {entry.fields["data_url"]}\n'
    # Code download
    if 'code_url' in entry.fields:
        md += f'code_url: {entry.fields["code_url"]}\n'
    # External website
    if 'external_url' in entry.fields:
        md += f'external_url: {entry.fields["external_url"]}\n'
    # Teaser image
    if 'teaser_img' in entry.fields:
        md += f'teaser_img: {entry.fields["teaser_img"]}\n'
    md += '---\n'


    with open(filename, 'w') as f:
        f.write(md)
        print(f'* Saved {filename}')


def pub_rank(entry):
    if 'venue_abbreviation' in entry.fields:
        venues = {
            'TPAMI': 90,
            'CVPR' : 80,
            'ICCV' : 80,
            'ECCV' : 80,
            'ACCV' : 60,
            'WACV' : 60,
            'AVSS' : 50,
            'TMM'  : 40,
            'CVWW' : 10,
            'ITSC' : 10
        }
        v = entry.fields['venue_abbreviation']
        if v in venues:
            return venues[v]
    return 0


def compare_bibentries(e1, e2):
    """Sort bibtex entries by year and importance of venue"""
    y1 = e1.fields['year']
    y2 = e2.fields['year']
    if y1 < y2:
        return -1
    elif y2 > y1:
        return +1
    else:
        r1 = pub_rank(e1)
        r2 = pub_rank(e2)
        if r1 < r2:
            return -1
        elif r2 > r1:
            return +1
        else:
            return 0


def parse_bibtex():
    args = parse_args()
    bibtex_data = bibtex.Parser().parse_file(args.bibtex_file)
    print(f'Dropping {len(bibtex_data.entries)} items to {args.output_folder}')
    # entries = [bibtex_data.entries[e] for e in bibtex_data.entries]
    # sorted_entries = sorted(entries, key=cmp_to_key(compare_bibentries))
    # print(sorted_entries)
    # # sorted_keys = sorted([e for e in bibtex_data.entries], key=lambda e: bibtex_data.entries[e].fields['year'], reverse=True)
    # # print(sorted_keys)

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
    #for k in sorted_keys:
    for k in bibtex_data.entries:
        dump_markdown(args.output_folder, bibtex_data.entries[k])


if __name__ == '__main__':
    parse_bibtex()