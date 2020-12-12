import os
import csv

# Access the file

data_path = os.path.join("Resources", "budget_data.csv")

months_count = int()
npl = float()       # Net total Profit/Loss
mtm_change = []     # change in profit and loss without the months
monthly_change = [] # Months and year list with parallel index to mtm_change

with open(data_path) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
   
    next(csvreader)

# setting variables up for the loop
# skipped the first month so including it in the total coung by starting months_count at 1
# prev_month allows us to subtract the previous month from the current in the loop. 
# prev_month is set to the first value in csvreader

    first_row = next(csvreader)
    prev_month = float(first_row[1])
    months_count += 1
    npl = prev_month

# Counting the months, adding the profit and Loss together
# separating the dates 
# change is change from the previous month to the present
# reset the prev_month to current month
# mtm_change is list of change per month
# monthly_change gives us an equal index for the months to mtm_change

    for x in csvreader:
        months_count += 1
        npl += float(x[1])
        change = float(x[1]) - prev_month
        prev_month = float(x[1])
        mtm_change.append(change)
        monthly_change.append(x[0])

# indexing the max/min to pull the month the max/min happened

max_index = mtm_change.index(max(mtm_change))
min_index = mtm_change.index(min(mtm_change)) 

avg_change = ((sum(mtm_change))/(len(mtm_change)))

# save results to variable to print and write to txt file 

analysis = (f"----------------------------------------------------------------\n"
"Financial Analysis\n"
"--------------------------------------\n"
f"Number of Months: {months_count}\n"
f"Net Total Profit/Loss: ${npl}\n"
f"Average Change: ${avg_change}\n"
f"Greatest Increase in Profits: {monthly_change[max_index]} ${mtm_change[max_index]}\n"
f"Greatest Decrease in Profits: {monthly_change[min_index]} ${mtm_change[min_index]}\n"
"----------------------------------------------------------------")
print(analysis)

output_path = os.path.join("analysis", "output.txt")

with open(output_path, "w") as txtfile:

    txtfile.write(analysis)

