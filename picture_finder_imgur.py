import os
import re

def find_urls_in_folder(folder_path, pattern1, pattern2):
    urls = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):  # 只處理 Markdown 檔案
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    urls += re.findall(pattern1, content)
                    urls += re.findall(pattern2, content)           
    return urls
    
    replace_dict = {
        r'https://i.imgur.com/.*\.jpg' : r'.*\.jpg',
        r'https://i.imgur.com/.*\.png' : r'.*\.png'
    }

    modified_content = re.sub(re.escape(old_string), new_string, content)

# 指定要搜尋的資料夾路徑
folder_path = './unprocessed_hackmd_file'

# 定義要尋找的網址模式
url_pattern1 = r'https://i.imgur.com/.*\.jpg'
url_pattern2 = r'https://i.imgur.com/.*\.png'

# 尋找符合網址模式的所有網址
found_urls = find_urls_in_folder(folder_path, url_pattern1, url_pattern2)

# 將結果輸出到一個.txt檔案
output_file = 'imgur_image_urls.txt'
with open(output_file, 'w') as file:
    for url in found_urls:
        file.write(url + '\n')

print(f'Have output the result to {output_file} file.')