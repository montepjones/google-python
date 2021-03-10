#!/usr/bin/env python3 

from pathlib import Path
import requests

def upload_image(file_name):
    print(file_name)
    url = "http://localhost/upload/"
    with open(file_name, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
        opened.close()

def main():
    path = Path.home()
    images = path / "supplier-data/images"
    [upload_image(e) for e in images.rglob("*.jpeg")]

if __name__ == "__main__":
    main()