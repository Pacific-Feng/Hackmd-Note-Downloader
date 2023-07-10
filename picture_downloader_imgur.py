import os
import urllib.request
from urllib.parse import urlparse

def download_image(url, output_directory):
    try:
        parsed_url = urlparse(url)
        file_name = os.path.basename(parsed_url.path)
        file_path = os.path.join(output_directory, file_name)
        
        if os.path.exists(file_path):
            print(f"File already exists: {file_path}")
            return

        urllib.request.urlretrieve(url, file_path)
        print(f"Downloaded {file_name}")
    except Exception as e:
        print(f"Failed to download {url} -> Error: {str(e)}")

file_path = "imgur_image_urls.txt"
output_directory = "downloaded_images"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

with open(file_path, "r") as file:
    urls = file.readlines()
urls = [url.strip() for url in urls]

for url in urls:
    download_image(url, output_directory)
