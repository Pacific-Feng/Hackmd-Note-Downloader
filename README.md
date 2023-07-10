# How to store a hackmd file to local

## Author

Min-Feng Hsieh ([Pacific-Feng](https://github.com/Pacific-Feng))

Jie-Hong Liu ([JieHong-Liu](https://github.com/JieHong-Liu))

Lu-Ying Wu

## Steps

### 0. Create a folder in your workstation

* Called **"Hackmd_Pic_Downloader"** (Or any othere name is fine)

### 1. Create cookies.json and put it in your folder

* See the [reference](https://github.com/JieHong-Liu/HackMD_IMG_downloader/tree/main)

### 2. Put all the file in your folder

* picture_finder_imgur.py
* picture_finder_hackmd.py
* picture_dowmloader_imgur.py
* picture_finder_hackmd.py
* picture_edit.py
* execution.sh

### 3. Create a folder to put your hackmd notes

* Called **"hackmd_file"** (MUST be this name!)

* You can use the function provided by Hackmd to download all of your notes

* Put all your notes in this folder

### 4. Run the command below

```shell=
sh execution.sh
```

### 5. Complete

* Now all the files in the "hackmd_file" are all brand new

* Also you can find a new dictionary called "downloaded_images" is generated, which store all the pictures you use in your note

* You can download the "hackmd_file" and "downloaded_images" from the workstation and upload them to your github for preservation