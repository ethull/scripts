#!/usr/bin/env bash

# convert all flacs in current directory to mp3 and rm flacs

# echo $PWD
# echo *.flac
# echo -e "\n"

# for file in "*.flac"; do ffmpeg -i $file -q:a 0 "${file%.*}.mp3"; done

for i in *.flac ; do 
    ffmpeg -i "$i" -q:a 0 "$(basename "${i/.flac}").mp3"
    #sleep 60
done
rm *.flac
