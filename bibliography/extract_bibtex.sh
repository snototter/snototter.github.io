#!/bin/bash --

venv=.venv3

if [[ ! -d "${venv}" ]]; then
  python3 -m venv "${venv}"
  source ${venv}/bin/activate
  pip3 install -U pip
  pip3 install pybtex
else
  source ${venv}/bin/activate
fi

python extract_bibtex.py theses.bib ../_theses
python extract_bibtex.py pubs-other.bib ../_pubs_workshops
#python extract_bibtex.py pubs-conferences.bib ../_pubs_conferences
#TODO ../_pubs_jrnl


