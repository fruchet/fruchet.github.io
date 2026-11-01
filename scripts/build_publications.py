#!/usr/bin/env python3
"""Convert _data/publications.bib into _data/publications.yml (newest first).

Requires: bibtexparser (v1), pyyaml.
"""
import re
import sys
from pathlib import Path

import bibtexparser
import yaml
from bibtexparser.bparser import BibTexParser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / "_data" / "publications.bib"
OUT = ROOT / "_data" / "publications.yml"

MONTHS = {m: i for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}


def clean(s):
    """Strip BibTeX braces and collapse whitespace."""
    return re.sub(r"\s+", " ", s.replace("{", "").replace("}", "")).strip()


def author_name(a):
    a = a.strip()
    if "," in a:
        last, first = a.split(",", 1)
        a = f"{first.strip()} {last.strip()}"
    return clean(a)


def month_number(entry):
    m = clean(entry.get("month", "")).lower()[:3]
    if m.isdigit():
        return int(m)
    return MONTHS.get(m, 0)


def venue(entry):
    for field in ("journal", "booktitle", "howpublished", "school", "publisher"):
        if entry.get(field):
            return clean(entry[field])
    if entry.get("eprint"):
        return "arXiv preprint"
    return ""


def convert(entry):
    db = BibDatabase()
    db.entries = [entry]
    raw = BibTexWriter().write(db).strip()

    eprint = clean(entry.get("eprint", ""))
    arxiv = f"https://arxiv.org/abs/{eprint}" if eprint and entry.get("archiveprefix", "arxiv").lower() == "arxiv" else ""
    out = {
        "key": entry["ID"],
        "title": clean(entry.get("title", "")),
        "authors": [author_name(a) for a in re.split(r"\s+and\s+", entry.get("author", "")) if a.strip()],
        "venue": venue(entry),
        "year": int(re.sub(r"\D", "", entry.get("year", "0")) or 0),
        "month": month_number(entry),
        "note": clean(entry.get("note", "")),
        "abstract": clean(entry.get("abstract", "")),
        "pdf": clean(entry.get("pdf", "")),
        "arxiv": clean(entry.get("arxiv", "")) or arxiv,
        "code": clean(entry.get("code", "")),
        "url": clean(entry.get("url", "")),
        "bibtex": raw,
    }
    return {k: v for k, v in out.items() if v not in ("", [], 0) or k == "year"}


def main():
    entries = []
    if BIB.exists():
        parser = BibTexParser(common_strings=True, ignore_nonstandard_types=False)
        with BIB.open(encoding="utf-8") as f:
            entries = bibtexparser.load(f, parser).entries
    pubs = [convert(e) for e in entries]
    pubs.sort(key=lambda p: (p["year"], p.get("month", 0)), reverse=True)
    with OUT.open("w", encoding="utf-8") as f:
        f.write("# Generated from publications.bib by scripts/build_publications.py. Do not edit.\n")
        yaml.safe_dump(pubs, f, allow_unicode=True, sort_keys=False, width=1000)
    print(f"Wrote {len(pubs)} publication(s) to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(main())
