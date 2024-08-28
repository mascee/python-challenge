#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#The total number of votes cast
# A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

import os
import csv 
election_data_csv = os.path.join("Resources", "election_data.csv")

#Open and read csv
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #Skip the header
    csv_header = next(csv_reader)

    #declare variables to work with data
    total_votes = 0
    candidates = {}
    winner = ""
    vote_count = 0

    #Loop through each row in election data
    for row in csv_reader:
        #count total votes
        total_votes += 1
        #take candidate info from row 3
        candidate = row[2]

        #Add candidate to the dictionary and update vote count
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

#Calculate total votes
analysis_txt = os.path.join("analysis", "PyPollAnalysis.txt")
with open(analysis_txt, mode="w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("______________________________________\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("______________________________________\n")


    #Caclulate the percemtage of votes and find the winner
    for candidate, votes in candidates.items():
        vote_percentage = (votes/total_votes) *100
        txt_file.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

        if votes > vote_count:
            vote_count = votes
            winner = candidate

    txt_file.write("________________________________________\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("________________________________________\n")



# Print results to the terminal

print("________________________________________\n")
print("Election Results\n")
print("______________________________________\n")
print(f"Total Votes: {total_votes}\n")
print("______________________________________\n")


#Caclulate the percemtage of votes and find the winner
for candidate, votes in candidates.items():
    vote_percentage = (votes/total_votes) *100
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    if votes > vote_count:
        vote_count = votes
        winner = candidate

print("________________________________________\n")
print(f"Winner: {winner}\n")
print("________________________________________\n")


