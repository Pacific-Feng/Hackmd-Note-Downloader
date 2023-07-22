#!/bin/bash
mkdir ./hackmd_file
rm -rf ./hackmd_file/*
python3 picture_finder_imgur.py
python3 picture_finder_hackmd.py
python3 picture_downloader_imgur.py
python3 picture_downloader_hackmd.py
python3 picture_edit.py
mv ./hackmd_file/Others/README.md ./hackmd_file/README.md
if [ -z "$(ls -A ./hackmd_file/Others)" ]; then
    rm -rf ./hackmd_file/Others
fi