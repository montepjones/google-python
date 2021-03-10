#!/usr/bin/env python3 

from pathlib import Path
import requests


def description_dict(file_name):
    lines = open(file_name).read().splitlines()
    keys = ['name', 'weight', 'description']
    post_dictionary = dict(zip(keys, lines))
    filter_numbers = filter(str.isdigit, post_dictionary["weight"])
    filter_numbers = "".join(filter_numbers)
    post_dictionary["weight"] = int(filter_numbers)
    post_dictionary["image_name"] = f"{Path(file_name).stem}.jpeg"
    return post_dictionary

def main():
    path = Path.home()
    images = path / "supplier-data/descriptions"
    dict_to_post = [description_dict(e) for e in images.rglob("*.txt")]
    r = requests.get('http://35.238.185.204/fruits/')
    for d in dict_to_post:
        requests.post('http://35.238.185.204/fruits/', json=d)

if __name__ == "__main__":
    main()