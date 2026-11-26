#!/usr/bin/env python3
"""Publish entry.png as the make.fun art entry image."""

from __future__ import annotations

import filecmp
import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"


def main() -> int:
    source = Path(__file__).resolve().parent / SOURCE_NAME
    if not source.is_file():
        print(
            "error: source image entry.png is missing; place entry.png next to main.py",
            file=sys.stderr,
        )
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        print(
            f"error: cannot create output directory {output_dir}: {exc}",
            file=sys.stderr,
        )
        return 1

    destination = output_dir / SOURCE_NAME
    try:
        shutil.copyfile(source, destination)
    except OSError as exc:
        print(
            f"error: cannot copy {source} to {destination}: {exc}",
            file=sys.stderr,
        )
        return 1

    size = destination.stat().st_size
    if size == 0:
        print(f"error: copied file {destination} is empty", file=sys.stderr)
        return 1

    if not filecmp.cmp(source, destination, shallow=False):
        print(
            f"error: copied file {destination} is not byte-identical to {source}",
            file=sys.stderr,
        )
        return 1

    print(f"output: {destination}")
    print(f"bytes written: {size}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
