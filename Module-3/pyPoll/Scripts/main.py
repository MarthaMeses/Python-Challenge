#Unit 3 Assigment - Py Me Up, Charlie
#pyPoll: Election Results
#@version 1.0
#@author Martha Meses

import os
import csv

filePath = "../Resources/election_data.csv"

row = 0
totalRows = 0
totalVotes = 0
totalCandidate = 0
winnerCandidate = 0
indexWinnerCandidate = 0
election_dataVoterID = []
election_dataCandidate= []
votesPerCandidate = []
percentVotesPerCandidate = []
nameCandidate = ["Khan", "Correy", "Li", "O'Tooley"]
totalCandidate = len(nameCandidate)

with open(filePath, "r") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        if totalRows == 0:
            totalRows += 1
        
        election_dataVoterID.append(row["Voter ID"])
        election_dataCandidate.append(row["Candidate"])
        totalVotes += 1
        totalRows += 1
    csvFile.close()

print("\nELECTION RESULTS\n")
print("------------------\n")
print(f'Total Votes:    {totalVotes:,}\n')
print("------------------\n")
row = 0
while row < totalCandidate:
    votesPerCandidate.append(election_dataCandidate.count(nameCandidate[row]))
    percentVotesPerCandidate.append((votesPerCandidate[row]*100)/totalVotes)
    print(f'{nameCandidate[row]}: {percentVotesPerCandidate[row]:.3f}% ({votesPerCandidate[row]:,})\n')
    row += 1
print("------------------\n")
winnerCandidate = max(votesPerCandidate)
indexWinnerCandidate = votesPerCandidate.index(winnerCandidate)
print(f'Winner: {nameCandidate[indexWinnerCandidate]}\n')
print("------------------\n\n")

row = 0
writeResultsFile = open("../Resources/electionResults.txt", "w")  
writeResultsFile.write("ELECTION RESULTS\n") 
writeResultsFile.write("------------------\n")
writeResultsFile.write(f'Total Votes:    {totalVotes:,}\n')
writeResultsFile.write("------------------\n")
while row < totalCandidate:
    writeResultsFile.write(f'{nameCandidate[row]}: {percentVotesPerCandidate[row]:.3f}% ({votesPerCandidate[row]:,})\n')
    row += 1
writeResultsFile.write("------------------\n")
writeResultsFile.write(f'Winner: {nameCandidate[indexWinnerCandidate]}\n')
writeResultsFile.write("------------------\n\n")
writeResultsFile.close() 
