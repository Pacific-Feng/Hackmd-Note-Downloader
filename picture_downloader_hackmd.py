import os
import requests
import json

def download_image(url, save_path):
    if os.path.exists(save_path):
        print(f"Image already exists: {save_path}")
        return

    response = requests.get(url, cookies=cookies_dict)

    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Downloaded the picture from {url}!")
    else:
        print(f"Failed to download the picture from {url}")

with open("cookies.json") as cookie:
    myCookies = json.load(cookie)

    # Transfer cookie list to dict
    cookies_dict = {}
    for cookie in myCookies:
        cookies_dict[cookie["name"]] = cookie["value"]

# Read the file containing image URLs
file_path = "./hackmd_image_urls.txt"
with open(file_path, "r") as file:
    image_urls = file.readlines()

# Download all images
for url in image_urls:
    url = url.strip()  # Remove whitespace and newline characters
    save_location = f"./downloaded_images/{url.split('/')[-1].strip()}"
    download_image(url, save_location)
