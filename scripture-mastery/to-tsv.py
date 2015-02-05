#!/usr/bin/env python
"""This will convert these text files to tab-separated-values appropriate for importing into various flashcard programs.
"""

def transform(fin,fout):
    with open(fin, "rUt") as fi:
        text = fi.read()

    text = text.replace("\n\n","$$")
    text = text.replace("\n","\t")
    text = text.replace("$$","\n")

    with open(fout,"wt") as fo:
        fo.write(text)


if __name__ == "__main__":
    import sys
    fin,fout = sys.argv[1:3]
    transform(fin,fout)
