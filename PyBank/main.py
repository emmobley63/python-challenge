import os
import csv

data_path = os.path.join("Resources", "budget_data.csv")

months_count = int()
npl = float()
date = []           # Months and year list
mtm_change = []     # change in profit and loss without the months. Should be able to apply this to a list of months skipping the first month
monthly_change = [] # creating a list for the monthl: change in profit

with open(data_path) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
   
    next(csvreader)

    first_row = next(csvreader)
    prev_month = float(first_row[1])
    months_count += 1
    npl = prev_month

# Counting the months, adding the profit and Loss together
# separating the dates and P/L into their own lists
    for x in csvreader:
        months_count += 1
        npl += float(x[1])
        date.append(x[0])
        change = float(x[1]) - prev_month
        prev_month = float(x[1])
        mtm_change.append(change)
        monthly_change.append(x[0])

# Creating a change in profit list (it will have 1 less month than the datelist
# because we cannot calculate the change for the first month)


    
#Need to creat a dictionary that pairs the months back together with 
#the respective change in profit/loss change mtm
    

max_index = mtm_change.index(max(mtm_change))
min_index = mtm_change.index(min(mtm_change)) 

avg_change = ((sum(mtm_change))/(len(mtm_change)))

#Instead of a dictionary. Trying to zip the different lists together and then if statement to print when index[1]=max,min
# or set variable to date.pop(0)


analysis = (f"----------------------------------------------------------------\n"
"Financial Analysis\n --------------------------------------\n"
f"Number of Months: {months_count}\n"
f"Net Total Profit/Loss: ${npl}\n"
f"Average Change: ${avg_change}\n"
f"Greatest Increase in Profits: {monthly_change[max_index]} ${mtm_change[max_index]}\n"
f"Greatest Decrease in Profits: {monthly_change[min_index]} ${mtm_change[min_index]}\n"
"----------------------------------------------------------------")
    

