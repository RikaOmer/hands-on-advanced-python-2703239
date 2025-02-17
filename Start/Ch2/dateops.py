# Example file for Advanced Python: Hands On by Joe Marini
# Working with date values

import json
from datetime import date


# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)


# TODO: The datetime module converts strings into dates fairly easily
dateobj = date.fromisoformat(weatherdata[0]['date'])
print(dateobj)

# TODO: Date objects give us information such as day of week (0=Monday, 6=Sunday)
print(dateobj.weekday())

# TODO: what was the warmest weekend day in the dataset?
def is_weekend_day(d):
    day = date.fromisoformat(d['date'])
    return (day.weekday() == 5 or day.weekday() == 6)

weekend_days = list(filter(is_weekend_day, weatherdata))
warmest_day = max(weekend_days, key=lambda d:d['tmax'])
print(date.fromisoformat(warmest_day['date']).strftime('%a,%d %b %Y'))

# The timedelta object provides an easy way of performing date math
# find the coldest day of the year and get the average temp for the following week
# coldest_day = min(weatherdata, key=lambda d: d['tmin'])
# convert the date to a Python date
# coldest_date = date.fromisoformat(coldest_day['date'])
# print(f"The coldest day of the year was {str(coldest_date)} ({coldest_day['tmin']})")

# TODO: Look up the next 7 days
