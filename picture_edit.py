# with open("/home/mfhsieh/Picture_Downloader/hackmd_backup/ISPD 2023 Alpha round.md", 'r') as file:
#     with open("/home/mfhsieh/Picture_Downloader/hackmd_backup/test.md", 'w') as f:
#         for line in file:
#             if "https://i.imgur.com/" in line:
#                 f.write(line.replace("https://i.imgur.com/",""))
#             elif "https://hackmd.io/_uploads/" in line:
#                 f.write(line.replace("https://hackmd.io/_uploads/",""))
#             else:
#                 f.write(line)

import os

infolder_path = './hackmd_file'
outfolder_path = './hackmd_backup'

for root, dirs, files in os.walk(infolder_path):
    for file in files:
            if file.endswith('.md'):  # 只處理 Markdown 檔案
                file_path = os.path.join(root, file)
                infile_name = file
                outfile_name = outfolder_path+"/"+infile_name
                with open(file_path, 'r', encoding='utf-8') as f_in:
                    with open(outfile_name, 'w') as f_out:
                        for line in f_in:
                            if "https://i.imgur.com/" in line:
                                f_out.write(line.replace("https://i.imgur.com/","../downloaded_images/"))
                            elif "https://hackmd.io/_uploads/" in line:
                                f_out.write(line.replace("https://hackmd.io/_uploads/",""))
                            else:
                                f_out.write(line)

print("\n----------------------------------")
print("      The process is done !")
print("----------------------------------")