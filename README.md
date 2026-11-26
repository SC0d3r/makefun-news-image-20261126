# make.fun art entry: news-image-20261126

`main.py` publishes `entry.png` as the entry image. It copies the file byte
for byte into `MAKEFUN_OUTPUT_DIR` (default `/output`), creating the directory
if needed, and checks that the copy is identical and non-empty.

Run it locally:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

`out/entry.png` will be an exact copy of the submitted image.
