import os
import pandas as pd
import csv
from itertools import groupby
from datetime import datetime

rootdir = ("C:\\Users\\elisk\\Desktop\\Data\\CHMU\\CHMU_historical_data\\inputs")

my_data  = []
headers =  ["DATA"] 
columns_data = ["Year", "Month", "Day", "Desc", "Value", "Station", "Variable"]
columns_metadata = ["Station_id", "Station_name", "Measure_start", "Measure_end", "Longitude", "Latitude", "Elevation", "Station"]

for subdir, dirs, files in os.walk(rootdir):
    for entry in files:
        #print(entry)
        if entry.endswith('SRA_N.csv'):
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
                            ### adding Time element in datetime format
                            time_elem = "/".join(line[0:3])
                            line.append(time_elem)
                            for item in line:
                                
                                #print(item)
                            # this one cannot be appended because of the datetime type???
                            # datetime_obj = datetime.strptime(time_elem, '%Y/%m/%d')
                            # line.append(datetime_obj)

                            my_data.append(line)
                            #print(line)
                            
    my_data.insert(0, columns_data)
    
    with open("C:\\Users\\elisk\\Desktop\\Data\\CHMU\\CHMU_historical_data\\outputs\\SRA_N.csv", 'w', newline='', encoding='cp1250') as csvfile:
        datawriter = csv.writer(csvfile, delimiter = ';', quotechar = '"')
        ## quotechar does not work!!!!
        for line in my_data:
            datawriter.writerow(line)
