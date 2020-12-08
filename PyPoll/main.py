import os
import csv

data_path = os.path.join("Resources", "election_data.csv")

with open(data_path) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
       
    for x in csvreader:   
       print(f"{x}")