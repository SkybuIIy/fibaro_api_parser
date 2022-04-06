# taken from https://www.geeksforgeeks.org/convert-json-to-csv-in-python/

import json
import csv
 
with open(input("full path to json file: ")) as json_file:
    jsondata = json.load(json_file)
 
data_file = open(input("full path to csv file to be written: "), 'w', newline='')
csv_writer = csv.writer(data_file)
 
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
 
data_file.close()
