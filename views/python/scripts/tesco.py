#!/usr/bin/env python3
import subprocess

with open("/home/nic/bin/imports/text_files/shopping.txt") as reader:
    for  line in reader:
        if line.strip() != "":
            search_term = "+".join(line.split())
            subprocess.run([
                "google-chrome",
                f"http://www.tesco.com/groceries/"
                f"Product/Search/Default.aspx?"
                f"searchBox={search_term}"
            ])
            print(search_term)
