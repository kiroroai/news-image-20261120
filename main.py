#!/usr/bin/env python3
"""Copy the entry.png sitting next to this script to the output directory.

Reads entry.png from the same directory as this script and writes it,
byte for byte, to <output>/entry.png, creating the output directory if
needed. Fully deterministic: the output is an exact copy of the input
on every run. Standard library only.
"""

import hashlib
import os
import shutil
import sys


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, destination)
    if sha256_of(source) != sha256_of(destination):
        print("error: copied file differs from source", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
