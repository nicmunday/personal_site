#!/usr/bin/env python3
import subprocess
import sys

if len(sys.argv) > 1:
    search_term = "+".join(sys.argv[1:])
    subprocess.run([
        "google-chrome",
        f"http://www.imdb.com/find?q={search_term}&s=tt"
    ])
    print(search_term)
else:
    print("You didn't include anything to search!")

