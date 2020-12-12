import os
import csv

#Access the file

data_path = os.path.join("Resources", "election_data.csv")

tv = 0           # Total Voters
voter = []       # list of voter ID
county = []      # list of county
candidate = []   # list of candidates
Kcount = int()   # Khan vote count
Ccount = int()   # Correy vote count
Lcount = int()   # Li vote count
Ocount = int()   # O'Tooley vote count


with open(data_path) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')

    next(csvreader)

    # Looping to count Total votes
    # Append the voter, county and candidate lists
    # Count votes for each candidate

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

# Calculate the % using the count and sum of votes
   
candidate_set = (set(candidate))
kper = float(Kcount/tv) *100
cper = float(Ccount/tv) *100
lper = float(Lcount/tv) *100
oper = float(Ocount/tv) *100

# Create list of candidates and a respectively indexed list of their percentages

canlist = ["Khan", "Correy", "Li", "O'Tooley"]
canper = [kper, cper, lper, oper]

#Find the max index to access the name of the winner

max_index = canper.index(max(canper))

winner = canlist[max_index]

# Set variable to print and write to txt file

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
        

    