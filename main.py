#!/usr/bin/env python3
"""news-image-20261120 entry: copy the broadsheet image to /output/entry.png.

Standard library only. The image is the entry.png beside this file; the
program copies it byte for byte, identically on every run. Outside the
grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
