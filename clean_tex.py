#!/usr/bin/env python3
"""
Delete all auxiliary LaTeX files, keeping only .tex and .pdf files.
"""

import os
import glob

# Common LaTeX auxiliary file extensions
aux_extensions = [
    '*.aux', '*.out', '*.toc', '*.lof', '*.lot',
    '*.fls', '*.fdb_latexmk', '*.synctex.gz', '*.bbl',
    '*.blg', '*.idx', '*.ind', '*.ilg', '*.nav', '*.snm',
    '*.vrb', '*.dvi', '*.ps', '*.bcf', '*.run.xml'
]

def clean_tex_files():
    """Remove all auxiliary LaTeX files from current directory."""
    deleted_count = 0

    for pattern in aux_extensions:
        for file in glob.glob(pattern):
            try:
                os.remove(file)
                print(f"Deleted: {file}")
                deleted_count += 1
            except Exception as e:
                print(f"Error deleting {file}: {e}")

    print(f"\nTotal files deleted: {deleted_count}")

if __name__ == "__main__":
    clean_tex_files()
