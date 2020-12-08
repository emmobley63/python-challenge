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
    z = 1
    

    for x in csvreader:
        months_count += 1
        npl += float(x[1])
        
        date.append(x[0])
        pl_list.append(float(x[1]))

    for y in range(1, (len(pl_list)-1)):
        change = pl_list[y] - pl_list[y-1]
        mtm_change.append(change)  
    
    
    # for y in pl_list:
    #     change = y[z]-y[z-1]
    #     mtm_change.append(change)
    #     z += 1


    print(f"The total number of months in the data set is {months_count}.")
        
    print(f"The net total amount of Profit/Losses is ${npl}.")

    print(f"{mtm_change}")    
    
    

