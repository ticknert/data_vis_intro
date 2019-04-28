# A program to visualize rainfall in Death Valley and Sitka

import csv
from datetime import datetime
from matplotlib import pyplot as plt

file_1 = 'death_valley_2014.csv'
file_2 = 'sitka_weather_2014.csv'
files = [file_1, file_2]
# Open the files
full_dates = []
full_rain = []
for file in files:
    with open(file_1) as file_obj:
        reader = csv.reader(file_obj)
        header_row = next(reader)
        for index, column_header in enumerate(header_row):
            print(index, column_header.strip())

        dates, rain = [], []
        for row in reader:
            try:
                date = datetime.strptime(row[0], "%Y-%m-%d")
                precipitation = int(row[19])
            except ValueError:
                print(files.index(file), date, "missing data")
            else:
                dates.append(date)
                rain.append(precipitation)
        
        full_dates.append(dates)
        full_rain.append(rain)

