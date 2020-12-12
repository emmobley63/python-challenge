# python-challenge
PyBank and PyPoll

PyBank

My company has a csv of the monthly profit/loss. I have two columns: "Date" and "Profit Loss" in budget_data.csv

I was looking to calulate the total number of months, net totale profit/loss, change in profit/loss over the entire period, greatest month of increase in profuts and the greatest month of loss.

My findings are published in the "output.txt" file in the "analysis" folder.

First, I etablished the variables to store the information. I skipped the first line to skip the titles of the csv. I then ran a for loop through the csv that allowed me to sum the net/profit loss, count the months, calculate the change per month, append the month and change list. I created the change in profit/loss list (mtm_change) to have the corresponding index to its respective month in (monthly_change). This allowed me to get the max index for both lists. 

To simplify printing my results, in the terminal and to the output I created the variable "analysis." 

The most alarming statistic in our findings was an average change in profit from month to month to be $-2315.12. This is suggesting that every month the profits are declining. I would suggest further inspection to see where the majority of the declination is. Is this a recent trend of decreased profits? Is the average brought down because of starting costs in the beginning? There is much more that could be drawn from the data to fully understand from where the decrease in profit is coming.


PyPoll

I was given a csv of the election results from a small rural town. The election_data.csv contains three columns: "Voter ID", "County", and "Candidate".

I was tasked with finding the total number of votes cast, a complete list of candidates, the percentage of votes per candidate, the count of votes per candidate, and the winner of the election.

My findings are published in the "output.txt" file in the "analysis" folder.

First, I set variables to store wanted information. I skipped the first line to skip the titles of the csv. I then created a for loop to count the total votes, cadidate list and count the amount of votes for each respective candidate. I used the counts to find the percentage of the vote for each candidate.  

I then created a candidate list that only contained the names of the candidates without redundancies. I created another list with the candidates'percentage of the vote in the same respective index of the list of their names. This made it so I can access the name of the candidate and their percentage of the vote with the same index. I can then equate the winner to the index of the largest percentage of the vote. 

Congratulations Khan for winning the election!

To simplify printing my results, in the terminal and to the output I created the variable "ol". 