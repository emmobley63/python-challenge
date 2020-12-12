import os
import csv

data_path = os.path.join("Resources", "election_data.csv")

tv = 0  
voter = []
county = []
candidate = []
Kcount = int()
Ccount = int()
Lcount = int()
Ocount = int()
results = {}

with open(data_path) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')

    next(csvreader)

    for x in csvreader:
        tv += 1
        voter.append(x[0])
        county.append(x[1])
        candidate.append(x[2])
        if x[2] == "Li":
            Lcount += 1
        if x[2] == "Khan":
            Kcount += 1
        if x[2] == "Correy":
            Ccount += 1
        if x[2] == "O'Tooley":
            Ocount += 1


   
candidate_set = (set(candidate))
kper = float(Kcount/tv) *100
cper = float(Ccount/tv) *100
lper = float(Lcount/tv) *100
oper = float(Ocount/tv) *100


canlist = ["Khan", "Correy", "Li", "O'Tooley"]
canper = [kper, cper, lper, oper]

max_index = canper.index(max(canper))

winner = canlist[max_index]

ol = ("Election Results\n" 
    "-----------------------\n"
    f"Total Votes: {tv}\n"
    "-----------------------\n"
    f"Khan: {kper:.3f}% ({Kcount})\n"
    f"Correy: {cper:.3f}% ({Ccount})\n"
    f"Li: {lper:.3f}% ({Lcount})\n"
    f"O'Tooley: {oper:.3f}% ({Ocount})\n"
    "-----------------------\n"
    f"Winner: {winner}\n"
    "-----------------------\n")

output_path = os.path.join("analysis", "output.txt")

with open(output_path, "w") as txtfile:

    print(ol)
    txtfile.write(ol)
        

    