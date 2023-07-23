# How to Store Hackmd Files Locally and Categorize by Tags

## Authors

Min-Feng Hsieh ([Pacific-Feng](https://github.com/Pacific-Feng))

Jie-Hong Liu ([JieHong-Liu](https://github.com/JieHong-Liu))

Lu-Ying Wu ([Lu-Ying, Wu](https://github.com/s95209))

<br>

## Reminder
   * Please make sure that your "README.md" is spelled correctly (alphabet, capitalization ...,etc )
<br>

## Steps

### 0. Prepare the Workspace

1. Create a folder on your workstation named **"Hackmd_Pic_Downloader"** (or any other name you prefer).

<br>

### 1. Configure Cookies

1. Create a file named **cookies.json** and place it in your workspace folder.
2. Refer to the [GitHub repository](https://github.com/JieHong-Liu/HackMD_IMG_downloader/tree/main) by JieHong-Liu for details on setting up the cookies.

<br>

### 2. Gather Required Files

1. Ensure the following files are present in your workspace folder:

   - picture_finder_imgur.py
   - picture_finder_hackmd.py
   - picture_downloader_imgur.py
   - picture_finder_hackmd.py
   - picture_edit.py
   - execution.sh

<br>

### 3. Organize Your Hackmd Notes

1. Create a folder named **"unprocessed_hackmd_file"** (Note: The folder name must be exactly as specified).
2. Download all your notes using the function provided by Hackmd and save them in this folder.

<br>

### 4. Execute the Process

1. Run the following command in the terminal:

```shell
   sh execution.sh
```

<br>

### 5. Process Completion

* All files in the **"hackmd_file"** folder are now updated.

* A new folder named **"downloaded_images"** is generated, containing all the images used in your notes.

* You can now download the "hackmd_file" and "downloaded_images" folders from your workstation and upload them to your GitHub for preservation.

<br><br><br>

----

### **- 1st edition** for New Feature:

* The program now supports tags used by Hackmd, for example below:

```markdown=
   ###### tags: SNPS Intern
```

* If you use the "tag" keyword in your notes, the program will automatically categorize the notes into different folders named after your tag for better organization.

<br>

**Author: Min-Feng Hsieh**  
**Date: 2023/07/22**

<br>

----

### **- 2nd edition** for New Feature:

* The program now supports that you can choose whether you want to categorize you notes by "tag" keyword

* Now the program will pop up the selection below:

```txt =
   Do you want to classify by the "tags" function?

   -> Enter "y" for YES
   -> Enter "n" for NO
```

* Enter **"y"** to categorize you notes by "tag" keyword

* Enter **"n"** to NOT categorize you notes by "tag" keyword

<br>

**Author: Min-Feng Hsieh**  
**Date: 2023/07/23**

<br>

---