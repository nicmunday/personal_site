#!/usr/bin/python3
from subprocess import run
from math import ceil
import prettytable

result = run(["ls", "-Ftr"], capture_output=True, text=True)

resultList=result.stdout.split("\n")
dirlist: list[str]=[]

for item in resultList:
    if item != "":
        dirlist.append(item)

if len(dirlist) == 0:
    print("\n                   "
          "No Items In Directory                 \n")

else:
    table = prettytable.PrettyTable()

    rows = ceil(len(dirlist)/4)
    table.add_column("1", dirlist[:rows])
    table.add_column("2", dirlist[rows:(rows*2)])
    table.add_column("3", dirlist[(rows*2):(rows*3)])
    finalcol = dirlist[rows*3:]
    while rows - len(finalcol) > 0:
        finalcol.append("")
    table.add_column("4", finalcol)
    

    table.header=False
    table.hrules=prettytable.ALL
    table.set_style(prettytable.SINGLE_BORDER)
    print(table)
