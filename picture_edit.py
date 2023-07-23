import os
import re

infolder_path = './unprocessed_hackmd_file'
outfolder_base_path = './hackmd_file'

def get_decision():
    print("\nDo you want to classify by the \"tags\" function?\n")
    print("-> Enter \"y\" for YES")
    print("-> Enter \"n\" for NO\n")
    print("Your decision = ", end="")
    decision = input()
    print("\n\n")
    return decision

def input_decision() :
    decision = get_decision()
    if (decision == "n" or decision == "N" or decision == "NO" or decision == "No" or decision == "no") :
        print("-> OK, we will NOT classify your code by \"tags\"")
        return "no"
    elif (decision == "y" or decision == "Y" or decision == "YES" or decision == "Yes" or decision == "yes") :
        print("-> OK, we will classify your code by \"tags\"")
        return "yes"
    else :
        print("-> Please input the correct word for distinguish!")
        input_decision()
    
decision = input_decision()

if (decision == "yes") :

    for root, dirs, files in os.walk(infolder_path):
        for file in files:
            if file.endswith('.md'):  # Only process Markdown files
                file_path = os.path.join(root, file)
                infile_name = file
                with open(file_path, 'r', encoding='utf-8') as f_in:
                    # Read the content of the file
                    content = f_in.read()
                    # Use regular expression to find the first tag (if any)
                    match = re.search(r'###### tags: `(.+?)`', content)
                    if match:
                        tag = match.group(1)
                    else:
                        tag = "Others"

                # Create the subfolder for the tag
                outfolder_path = os.path.join(outfolder_base_path, tag)
                os.makedirs(outfolder_path, exist_ok=True)

                # Generate the output file name
                outfile_name = os.path.join(outfolder_path, infile_name)

                with open(file_path, 'r', encoding='utf-8') as f_in:
                    with open(outfile_name, 'w') as f_out:
                        for line in f_in:
                            if "https://i.imgur.com/" in line:
                                f_out.write(line.replace("https://i.imgur.com/", "../../downloaded_images/"))
                            elif "https://hackmd.io/_uploads/" in line:
                                f_out.write(line.replace("https://hackmd.io/_uploads/", "../../downloaded_images/"))
                            else:
                                f_out.write(line)

    print("\n----------------------------------")
    print("      The process is done !")
    print("----------------------------------\n")

elif (decision == "no") :
    for root, dirs, files in os.walk(infolder_path):
        for file in files:
                if file.endswith('.md'):  # 只處理 Markdown 檔案
                    file_path = os.path.join(root, file)
                    infile_name = file
                    outfile_name = outfolder_base_path+"/"+infile_name
                    with open(file_path, 'r', encoding='utf-8') as f_in:
                        with open(outfile_name, 'w') as f_out:
                            for line in f_in:
                                if "https://i.imgur.com/" in line:
                                    f_out.write(line.replace("https://i.imgur.com/","../downloaded_images/"))
                                elif "https://hackmd.io/_uploads/" in line:
                                    f_out.write(line.replace("https://hackmd.io/_uploads/","../downloaded_images/"))
                                else:
                                    f_out.write(line)

    print("\n----------------------------------")
    print("      The process is done !")
    print("----------------------------------")
