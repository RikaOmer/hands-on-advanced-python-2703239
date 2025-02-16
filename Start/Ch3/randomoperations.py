# Example file for Advanced Python: Hands On by Joe Marini

import json
import random
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# get the first 30 days in the dataset
month_data = weatherdata[0:30]

# TODO: the shuffle() function will randomly shuffle a list in-place
random.shuffle(month_data)


# TODO: use choice() and choices() to get random items, but beware that
# these functions can produce duplicate results
rnd_day = random.choice(month_data)
rnd_days = random.choices(month_data, k=4)


# TODO: the sample() function will choose random items with no duplicates

rnd_days = random.sample(month_data, k=4)
