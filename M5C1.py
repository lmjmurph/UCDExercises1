# Import date
from datetime import date, datetime, timedelta, timezone
from dateutil import tz
#import pandas
import pandas as pd
import requests


# import pickle to enable opening pickle file
import pickle
infile = open('florida_hurricane_dates.pkl','rb')
florida_hurricane_dates = pickle.load(infile)
infile.close()

# Exercise 1
# Create a date object for May 9th, 2007
start = date(2007, 5, 9)

# Create a date object for December 13th, 2007
end = date(2007, 12,13)

# Subtract the two dates and print the number of days
print((end - start).days)


# Exercise 2
# A dictionary to count hurricanes per calendar month
hurricanes_each_month = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0,
                         7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

# Loop over all hurricanes
for hurricane in florida_hurricane_dates:
    # Pull out the month
    month = hurricane.month
    # Increment the count in your dictionary by one
    hurricanes_each_month[month] += 1

print(hurricanes_each_month)

# Exercise 3
# Print the first and last scrambled dates
print(florida_hurricane_dates[0])
print(florida_hurricane_dates[-1])

# Put the dates in order
dates_ordered = sorted(florida_hurricane_dates)

# Print the first and last ordered dates
print(dates_ordered[0])
print(dates_ordered[-1])


# Exercise 4
# Import datetime
from datetime import datetime

# Create a datetime object
dt = datetime(2017, 10, 1, 15, 26, 26)

# Print the results in ISO 8601 format
print(dt.isoformat())


# Exercise 5
# Create a datetime object
dt = datetime(2017, 12, 31, 15, 19, 13)

# Print the results in ISO 8601 format
print(dt.isoformat())


# Exercise 6

# Create a datetime object
dt = datetime(2017, 12, 31, 15, 19, 13)

# Replace the year with 1917
dt_old = dt.replace(year = 1917)

# Print the results in ISO 8601 format
print(dt_old)

# Exercise 7
# Create dictionary to hold results
trip_counts = {'AM': 0, 'PM': 0}

# Loop over all trips
capital_onebike = pd.read_csv("capital-onebike.csv")
print(capital_onebike)
capital_onebike['Start date'] = pd.to_datetime(capital_onebike['Start date'])
capital_onebike['End date'] = pd.to_datetime(capital_onebike['End date'])
onebike_datetimes = capital_onebike.iloc[:,0:2].to_dict("records")
print(onebike_datetimes)


for trip in onebike_datetimes:
    # Check to see if the trip starts before noon
    if trip['Start date'].hour < 12:
        # Increment the counter for before noon
        trip_counts['AM'] += 1
    else:
        # Increment the counter for after noon
        trip_counts['PM'] += 1

print(trip_counts)

# Exercise 8

# Import the datetime class
from datetime import datetime

# Starting string, in MM/DD/YYYY HH:MM:SS format
s = '12/15/1986 08:00:00'

# Write a format string to parse s
fmt = '%m/%d/%Y %H:%M:%S'

# Create a datetime object d
d = datetime.strptime(s, fmt)

# Print d
print(d)

# Exercise 9

# Write down the format string
fmt = "%Y-%m-%d %H:%M:%S"

# Initialize a list for holding the pairs of datetime objects
onebike_datetimes = []

# reset capital_onebike back to original format
capital_onebike = pd.read_csv("capital-onebike.csv")
print(type(capital_onebike))

onebike_datetime_strings = list(capital_onebike[['Start date', 'End date']].to_records(index=False))
print (onebike_datetime_strings)

# Loop over all trips
for (start, end) in onebike_datetime_strings:
    trip = {'start': datetime.strptime(start, fmt),
            'end': datetime.strptime(end, fmt)}

    # Append the trip
    onebike_datetimes.append(trip)

print(trip)

# Exercise 10

# Pull out the start of the first trip
first_start = onebike_datetimes[0]['start']

# Format to feed to strftime()
fmt = "%Y-%m-%dT%H:%M:%S"

# Print out date with .isoformat(), then with .strftime() to compare
print(first_start.isoformat())
print(first_start.strftime(fmt))


# Exercise 11

data=requests.get("http://api.open-notify.org/iss-now.json")
data= data.json()
print(data['iss_position'])

# Exercise 12

# Start on March 12, 2017, midnight, then add 6 hours
start = datetime(2017, 3, 12, tzinfo = tz.gettz('America/New_York'))
end = start + timedelta(hours=6)
print(start.isoformat() + " to " + end.isoformat())

# How many hours have elapsed?
print((end - start).total_seconds()/(60*60))

# What if we move to UTC?
print((end.astimezone(timezone.utc) - start.astimezone(timezone.utc)).total_seconds()/(60*60))


# Exercise 12 - See offset on same date over several years

# Create starting date
dt = datetime(2000, 3, 29, tzinfo = tz.gettz("Europe/London"))

# Loop over the dates, replacing the year, and print the ISO timestamp
for y in range(2000, 2011):
  print(dt.replace(year = y).isoformat())