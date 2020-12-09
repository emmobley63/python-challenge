import os
import csv

data_path = os.path.join("Resources", "election_data.csv")

with open(data_path) as datafile:
    csvreader = csv.reader(datafile, delimiter=',')

    next(csvreader)

    tv = 0  
    voter = []
    county = []
    candidate = []
    Kcount = int()
    Ccount = int()
    Lcount = int()
    Ocount = int()

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
    cancount = {"Khan": kper, 
                "Correy": cper, 
                "Li": lper, 
                "O'Tooley": oper}
    
    # for key, value in cancount.items():
        


    # winner = "O'Tooley"
    # if kper > 50 or (kper > oper)
    #     winner = "Khan"
    # if cper > 50 or ()
    #     winner = "Correy"
    # if lper > 50
    #     winner = "Li"
    


    print("Election Results") 
    print("-----------------------")
    print(f"Total Votes: {tv}")
    print("-----------------------")
    print(f"Khan: {kper}% ({Kcount})")
    print(f"Correy: {cper}% ({Ccount})")
    print(f"Li: {lper}% ({Lcount})")
    print(f"O'Tooley: {oper}% ({Ocount})")
    print("-----------------------")
    print(f"Winner: {winner}")
    print("-----------------------")