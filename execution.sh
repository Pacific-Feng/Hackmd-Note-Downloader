#!/bin/bash
mkdir ./hackmd_backup
python3 picture_finder_imgur.py
python3 picture_finder_hackmd.py
python3 picture_downloader_imgur.py
python3 picture_downloader_hackmd.py
python3 picture_edit.py
mv ./hackmd_backup/* ./hackmd_file
rm -rf ./hackmd_backup