import os
import pandas as pd
import csv
from itertools import groupby

rootdir = ("\\inputs")

my_data  = []
headers =  ["DATA"] 
columns_data = ["Year", "Month", "Day", "Desc", "Value", "Station", "Variable"]
columns_metadata = ["Station_id", "Station_name", "Measure_start", "Measure_end", "Longitude", "Latitude", "Elevation", "Station"]

for subdir, dirs, files in os.walk(rootdir):
    for entry in files:
        if entry.endswith('_SRA_N.csv'):
            file_path = os.path.join(subdir, entry)
            last_header = ""
            is_header = False
            row_index = 0
            with open(file_path,  encoding="cp1250") as csvfile:
                csv_lines = csv.reader(csvfile, delimiter=";")
                for line in csv_lines:
                    if len(line) > 0:
                        if len(line) == 1:
                            last_header = line[0]
                            row_index = 0
                        row_index += 1
                        is_header = len(line) == 1
                        if last_header in headers and not is_header and row_index > 2:
                            file_index = len(line)
                            station = entry.split('_')[0]
                            variable = entry.split('_')[1]
                            line.append(station)
                            line.append(variable)
                            my_data.append(line)
    my_data.insert(0, columns_data)
    #my_data["TimeStamp"] = my_data["Year"] + my_data["/"] + my_data["Month"] + my_data["/"] + my_data["Day"]
    #print(my_data)

    with open("\\outputs\\SRA_N_2.csv", 'w', newline='', encoding='cp1250') as csvfile:
        datawriter = csv.writer(csvfile, delimiter = ';')
        for line in my_data:
            datawriter.writerow(line)
