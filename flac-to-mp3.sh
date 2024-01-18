#!/usr/bin/env bash

# convert all flacs in current directory to mp3

for i in *.flac ; do 
    ffmpeg -i "$i" -q:a 0 "$(basename "${i/.flac}").mp3"
    #sleep 60
done
