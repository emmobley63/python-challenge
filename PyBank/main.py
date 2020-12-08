import os
import csv

data_path = os.path.join("Resources", "budget_data.csv")

with open(data_path) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
   
    next(csvreader)

    months_count = int()
    npl = float()
    pl_list = []
    mtm_change = []
    z = 1
    

    for x in csvreader:
        months_count += 1
        npl += float(x[1])
        
        pl_list.append(float(x[1]))
        
    for y in pl_list:
        mtm_change.append(float(y[z]-y[z-1])) 


    print(f"The total number of months in the data set is {months_count}.")
        
    print(f"The net total amount of Profit/Losses is ${npl}.")

    print(f"{change_list}")    
    
    

