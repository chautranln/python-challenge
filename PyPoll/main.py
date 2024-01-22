import os
import csv

ElectionDataCSV = os.path.join("PyPoll", "Resources", "election_data.csv")

#Set variables
TotalVotes = 0
CandidateVotes = []
Results = []

with open(ElectionDataCSV) as BudgetFile:
    csvreader = csv.reader(BudgetFile, delimiter=",")
    header = next(csvreader)

#Total number of votes cast
    for row in csvreader:
        TotalVotes += 1
       
#List of candidates who received votes, % they each won, total number of votes they each won
        candidate = row[2]
        if candidate not in CandidateVotes:
            CandidateVotes[candidate] = 1
        else:
            CandidateVotes[candidate] += 1 

for candidate, votes in CandidateVotes.items():
    percentage = (votes/TotalVotes)
    Results.append(f"{candidate}: ({percentage:.2%}%) ({votes})")

#Winner of the election
winner = max(CandidateVotes, key=CandidateVotes.get) 

#Output file
Output = os.path.join("PyPoll", "analysis", "Election_results.txt")

with open(Output, "w") as OutputFile:
    OutputFile.write("Election Results\n")
    OutputFile.write("-------------------------\n")
    OutputFile.write(f"Total Votes: {TotalVotes}\n")
    OutputFile.write("-------------------------\n")
    for result in Results:
        OutputFile.write(f"{Results}\n")
    OutputFile.write("-------------------------\n")
    OutputFile.write(f"Winner: {winner}\n")
    OutputFile.write("-------------------------")




 


