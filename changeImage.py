#!/usr/bin/env python3 

from pathlib import Path
from PIL import Image

def rotate_and_resize(file_name):
    im = Image.open(file_name)
    # converting to jpg 
    rgb_im = im.convert("RGB") 
    out_file = Path(file_name).stem
    out_directory = Path(file_name).parent
    print(f"{out_directory}/{out_file}.jpeg")
    rgb_im.resize((600,400)).save(f"{out_directory}/{out_file}.jpeg")

def main():
    path = Path.home()
    images = path / "supplier-data/images"
    [rotate_and_resize(e) for e in images.rglob("*.tiff")]

if __name__ == "__main__":
    main()