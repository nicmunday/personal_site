#!/usr/bin/env python3
import feedparser

class LatestWeather:
    def __init__(self):
        feed = feedparser.parse("https://weather-broker-cdn.api.bbci.co.uk/en/observation/rss/2633749")

        weather_data = feed.entries[0].title.split()
        # Format and chop as necessary
        publist = feed.entries[0].published.split()
        #print (publist)
        self.published = f"{publist[0][:-1]} {publist[1]} {publist[2]} {publist[4][:-3]}"

        self.day = weather_data[0]
        self.time = weather_data[2]
        if len(weather_data) == 7:
            self.conditions = weather_data[4][:-1]
            self.temp = weather_data[5]
        else:
            self.conditions = weather_data[4] + " " + weather_data[5][:-1]
            self.temp = weather_data[6]


