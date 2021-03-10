#!/usr/bin/env python3

import reports
import emails
import os
from pathlib import Path
import datetime



def description_dict(file_name):
    lines = open(file_name).read().splitlines()
    keys = ['name', 'weight', 'description']
    post_dictionary = dict(zip(keys, lines))
    del post_dictionary['description']
    return post_dictionary

def main():
    now = datetime.datetime.now()
    todays_date = now.strftime("%B %d, %Y")
    path = Path.home()
    text_files = path / "supplier-data/descriptions"
    list_of_descriptions = [description_dict(e) for e in text_files.rglob("*.txt")]
    flatten_list = []
    for new_dict in list_of_descriptions:
        for k, v in new_dict.items():
            flatten_list.append(f"{k}: {v}")    
        flatten_list.append('')

    reports.generate("/tmp/processed.pdf", f"Processed Update on {todays_date}", "<br/>".join(flatten_list))

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")

    emails.send(message)


if __name__ == "__main__":
    main()