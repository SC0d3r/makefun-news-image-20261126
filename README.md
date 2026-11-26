# make.fun art entry: news-image-20261126

`main.py` publishes `entry.png` as the entry image. It copies the file byte
for byte into `MAKEFUN_OUTPUT_DIR` (default `/output`), creating the directory
if needed, then prints the output path and the number of bytes written. It
checks that the copy is non-empty and byte-identical to the source, and exits
non-zero with a clear error if the source is missing or either check fails.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`out/entry.png` will be an exact copy of the submitted image.
