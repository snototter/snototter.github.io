#!/usr/bin/python
# coding=utf-8
"""
Parse my bibtex file and create jekyll-friendly collection entries.
"""
import argparse
import os
import sys
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
        # C("\\'{a}", '&aacute;'), ("{\\' a}", '&aacute;'), ("{\\'a}", '&aacute;'),
        # ("\\'{A}", '&Aacute;'), ("{\\' A}", '&Aacute;'), ("{\\'A}", '&Aacute;'),
        # L("\\'{a}", '&aacute;'), ("{\\' a}", '&aacute;'), ("{\\'a}", '&aacute;'),
        # ("\\'{A}", '&Aacute;'), ("{\\' A}", '&Aacute;'), ("{\\'A}", '&Aacute;'),
        # N("\\'{a}", '&aacute;'), ("{\\' a}", '&aacute;'), ("{\\'a}", '&aacute;'),
        # ("\\'{A}", '&Aacute;'), ("{\\' A}", '&Aacute;'), ("{\\'A}", '&Aacute;'),
        # R("\\'{a}", '&aacute;'), ("{\\' a}", '&aacute;'), ("{\\'a}", '&aacute;'),
        # ("\\'{A}", '&Aacute;'), ("{\\' A}", '&Aacute;'), ("{\\'A}", '&Aacute;'),
        # S("\\'{a}", '&aacute;'), ("{\\' a}", '&aacute;'), ("{\\'a}", '&aacute;'),
        # ("\\'{A}", '&Aacute;'), ("{\\' A}", '&Aacute;'), ("{\\'A}", '&Aacute;'),
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
        ('{', ''), ('}', '')
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
    tokens = p.first_names + p.middle_names + p.prelast_names + p.last_names
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
    filename = os.path.join(output_folder, f'{year}-{key}.md')
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
    md += f'authors: {authors}\n'
    if entry.type in ['phdthesis', 'mscthesis', 'bscthesis']:
        thesis_type = {
            'phdthesis': 'PhD thesis',
            'mscthesis': "Master's thesis",
            'bscthesis': "Bachelor's thesis"
        }
        md += f'thesis_type: {thesis_type[entry.type]}\n'
        venue = entry.fields['school']
    elif entry.type in ['inproceedings']:
        venue = 'In ' + entry.fields['booktitle']
    elif entry.type in ['article']:
        venue = entry.fields['journal']
        #TODO + vol/issue, etc

    venue = html_escape(venue)
    md += f'venue: {venue}\n'
    
    # Add download/further links
    if 'venue_url' in entry.fields:
        md += f'venue_url: {entry.fields["venue_url"]}\n'
    if 'pdf_url' in entry.fields:
        md += f'pdf_url: {entry.fields["pdf_url"]}\n'
    if 'publisher_url' in entry.fields:
        md += f'publisher_url: {entry.fields["publisher_url"]}\n'
    if 'video_url' in entry.fields:
        md += f'video_url: {entry.fields["video_url"]}\n'
    if 'code_url' in entry.fields:
        md += f'code_url: {entry.fields["code_url"]}\n'
    if 'slide_url' in entry.fields:
        md += f'slide_url: {entry.fields["slide_url"]}\n'
    md += '---\n'


    with open(filename, 'w') as f:
        f.write(md)
        print(f'* Saved {filename}')


def parse_bibtex():
    args = parse_args()
    bibtex_data = bibtex.Parser().parse_file(args.bibtex_file)
    print(f'Dropping {len(bibtex_data.entries)} items to {args.output_folder}')
    #print([bibtex_data.entries[e] for e in bibtex_data.entries])
    #sorted_keys = sorted([e for e in bibtex_data.entries], key=lambda e: bibtex_data.entries[e].fields['year'], reverse=True)
    #print(sorted_keys)
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)
    #for k in sorted_keys:
    for k in bibtex_data.entries:
        dump_markdown(args.output_folder, bibtex_data.entries[k])


if __name__ == '__main__':
    parse_bibtex()