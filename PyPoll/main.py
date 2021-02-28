import os
import csv
import sys

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    # declaring/initializing variables
    total_votes = 0
    winner = 'N/A'
    most_votes = 0
    candidates = {"name","votes","votepercent"}

    for row in csvreader:
        total_votes += 1
        
        if row[2] not in candidates["name"]:
            # get candidate names from index 2 in each row
            candidates[row[2]] = 0

        # numvotes = vote count per candidate
        candidates["votes"] += 1

        # percent of votes = votes / total
        candidates["votepercent"] = ({candidates["votes"]} / total_votes) * 100
        
       


# Output to terminal

print("Election Results")
print("-------------------------")
print("Total Votes: ", total_votes)
print("-------------------------")
# Candidate Name: VotesPercent% (NumVotes)

print("-------------------------")
#print("Winner: ", winner)
print("-------------------------")

# Output to text file

sys.stdout = open("budget_analysis.txt", "w")

print("Election Results")
print("-------------------------")
print("Total Votes: ", total_votes)
print("-------------------------")
# Candidate Name: VotesPercent% (NumVotes)

print("-------------------------")
#print("Winner: ", winner)
print("-------------------------")

sys.stdout.close()