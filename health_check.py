#!/usr/bin/env python3
import emails
import os
import psutil
import shutil
import socket


def send_email(subject):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = " Please check your system and resolve the issue as soon as possible."
    message = emails.generate(sender, receiver, subject, body)
    emails.send(message)



def main():
    # send_email("This is a test!")
    total, used, free = shutil.disk_usage(__file__)
    cpu_usage = psutil.cpu_percent()
    print(cpu_usage)
    if psutil.cpu_percent() > 80:
        send_email("Error - CPU usage is over 80% ")
        
    if .8 * total < free:
        send_email("Error - Available disk space is less than 20%")

    if psutil.virtual_memory().available < 524288000:
        send_email("Error - Available memory is less than 500MB") 
 
    # IP lookup from hostname
    try:
        ip = socket.gethostbyname("localhost")
    except socket.gaierror as e:
        send_email(" Error - localhost cannot be resolved to 127.0.0.1")

if __name__ == "__main__":
    main()