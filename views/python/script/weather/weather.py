#!//usr/bin/env python3
import datetime
from imports import latest_weather
from imports import threedayweather
import prettytable
import subprocess


weather = threedayweather.ThreeDayWeather()
today = weather.today()
tomorrow = weather.tomorrow()
day_after = weather.day_after_tomorrow()

table = prettytable.PrettyTable()
table.header = False
table.hrules = prettytable.FRAME
table.vrules = prettytable.FRAME
table.set_style(prettytable.DOUBLE_BORDER)

latest = latest_weather.LatestWeather()
table.add_row([f"{latest.day} {latest.time}", f"{latest.conditions} {latest.temp}"])

table.add_row(["",""])

table.add_row([today["day"], today["description"]])
table.add_row([f"{today['max']} {today['min']}", today["wind"]])
table.add_row([today["sunrise"], today["sunset"]])
table.add_row(["",""])
table.add_row([tomorrow["day"], tomorrow["description"]])
table.add_row([f"{tomorrow['max']} {tomorrow['min']}", today["wind"]])
table.add_row([tomorrow["sunrise"], tomorrow["sunset"]])
table.add_row(["",""])
table.add_row([day_after["day"], day_after["description"]])
table.add_row([f"{day_after['max']} {day_after['min']}", today["wind"]])
table.add_row([day_after["sunrise"], day_after["sunset"]])

table.add_row(["",""])

now = "Now: " + datetime.datetime.now().strftime("%H:%M")
table.add_row([now, weather.published])

print(table)


#input("press any key to refresh")

#subprocess.run(["/home/nic/bin/weather"])
#subprocess.run(["/home/nic/bin/today", "-w"])
