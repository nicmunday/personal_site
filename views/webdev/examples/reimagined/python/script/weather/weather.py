#!/usr/bin/env python3
import sys
import prettytable
from imports import latest_weather
from imports import threedayweather

table = prettytable.PrettyTable()
table.header = False
table.hrules = prettytable.FRAME
table.vrules = prettytable.FRAME
table.set_style(prettytable.DOUBLE_BORDER)

def add_row(day):

    table.add_row([day["day"],
                   day["description"]])
    table.add_row([f"{day['max']} {day['min']}",
                   day["wind"]])
    table.add_row([day["sunrise"],
                   day["sunset"]])
    table.add_row(["", ""])

def add_col(day):
    table.add_column("",[day["day"],
                         "",
                         day["description"],
                         day["max"],
                         day["min"],
                         day["wind"],
                         day["sunrise"],
                         day["sunset"],
                         ""])


latest = latest_weather.LatestWeather()
weather = threedayweather.ThreeDayWeather()

days = [
    weather.today(),
    weather.tomorrow(),
    weather.day_after_tomorrow()
]

if "-v" in sys.argv:
    table.add_row([f"{latest.day} {latest.time}",
                   f"{latest.conditions} {latest.temp}"])
    table.add_row(["",""])

    [add_row(day) for day in days]
    table.add_row([weather.now, weather.published])

else:
    [add_col(day) for day in days]
    table.add_column("",[
        "Latest",
        "",
        "",
        latest.time,
        latest.conditions,
        latest.temp,
        "",
        "",
        ""
    ])

    table.add_row(["","",weather.now, weather.published])

print(table)
