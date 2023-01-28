#!/usr/bin/env python3
import subprocess
import pathlib
import webbrowser

current_path = pathlib.Path(__file__).parent
shopping_file = current_path.joinpath("imports",
                                       "text_files",
                                       "shopping.txt")

tesco_url = "http://www.tesco.com/" \
            "groceries/Product/Search/" \
            "Default.aspx?searchBox="

[webbrowser.open_new_tab(tesco_url + '+'.join(line.split()))
 for line in shopping_file.read_text().splitlines()]
