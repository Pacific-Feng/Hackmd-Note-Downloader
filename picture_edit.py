import os
import re

infolder_path = '././unprocessed_hackmd_file'
outfolder_base_path = './hackmd_file'

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