 # Example file for Advanced Python: Hands On by Joe Marini
# Using the statistics package

import json
import statistics

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# select the days from the summer months from all the years
summers = ["-06-","-07-","-08-"]
summer_months = [d for d in weatherdata if any([month in d['date'] for month in summers])]
print(f"Data for {len(summer_months)} summer days")

# TODO: calculate the mean for both min and max temperatures
max_temps = [d['tmax'] for d in summer_months]
min_temps = [d['tmin'] for d in summer_months]
print(max_mean := statistics.mean(max_temps))
print(min_mean := statistics.mean(min_temps))

# TODO: calculate the median values for min and max temperatures
print(statistics.median(max_temps))
print(statistics.median(min_temps))

# TODO: use the standard deviation function to find outlier temperatures
