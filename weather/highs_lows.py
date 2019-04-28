# Use weather data from www.wunderground.com/history/
# Actually got the data from www.nostartch.com/pythoncrashcourse/

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Open the .csv file
filename = 'sitka_weather_2014.csv'
with open(filename) as file_obj:
    reader = csv.reader(file_obj)
    header_row = next(reader) # Could also do next(csv.reader(file_obj))

    # Print each item in the header along with an index number using enumerate()
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header.strip())

    # Pull the date, and high and low temperature from each day.
    dates, highs, lows = [], [], []
    for row in reader:
        date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# Plot the data.
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.75)
plt.plot(dates, lows, c='blue', alpha=0.75)
plt.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)

# Format the plot.
plt.title("Daily High and Low Temperatures - 2014", fontsize=20)
plt.xlabel("", fontsize=16)
fig.autofmt_xdate() # To make the dates fit on the bottom without overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()