import os
import csv

data_path = os.path.join("Resources", "budget_data.csv")

with open(data_path) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
   
    next(csvreader)

    months_count = int()
    npl = float()
    pl_list = [] #Profit Loss numbers without the months
    date = []   #Months and year list
    mtm_change = [] #change in profit and loss without the months. Should be able to apply this to a list of months skipping the first month
    monthly_change = {} #creating a dict for the monthl: change in profit
    

# Counting the months, adding the profit and Loss together
# separating the dates and P/L into their own lists
    for x in csvreader:
        months_count += 1
        npl += float(x[1])
        date.append(x[0])
        pl_list.append(float(x[1]))

# Creating a change in profit list (it will have 1 less month than the month index
# because we cannot calculate the change for the first month)

    for y in range(1, (len(pl_list)-1)):
        change = pl_list[y] - pl_list[y-1]
        mtm_change.append(change)  
    
#Need to creat a dictionary that pairs the months back together with 
#the respective change in profit/loss change mtm


    avg_change = ((sum(mtm_change))/(len(mtm_change)))
    max_change = max(mtm_change)

    print(f"The total number of months in the data set is {months_count}.")
        
    print(f"The net total amount of Profit/Losses is ${npl}.")

    
    print(f"Average Change: ${avg_change}")    
    print(f"{max_change}")  
    
#This was the original way I thought to make the loop
#but this is accessing each item in the list and trying 
#to index these float items
# for y in pl_list:
#     change = y[z]-y[z-1]
#     mtm_change.append(change)
#     z += 1
