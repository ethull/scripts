#!/usr/bin/env bash

# convert all mp3 files in current and child dirs to flac and delete mp3 files

shopt -s globstar
for f in **/*.flac; do
    #flac -cd "$f" | lame -b 320 - "${f%.*}".mp3 # && rm "$f"
    ffmpeg -i "$f" -q:a 0 "${f%.*}".mp3 && rm "$f"
done
