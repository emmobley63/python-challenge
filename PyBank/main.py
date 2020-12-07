import os
import csv

data_path = os.path.join("Resources", "budget_data.csv")

with open(data_path) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
   
    next(csvreader)

    months_count = int()

    for x in csvreader:
        months_count += 1
    
    print(f"The total number of months in the data set is {months_count}.")
    
    npl = float()

    for y in csvreader:
        float(y.index[1])
        print(f"{float(y.index[1])}")
    
    print(f"The net total amount of Profit/Losses is ${npl}.")

    
    
    
    # months_count = len(csvreader)
    # print(f"{months_count}")
