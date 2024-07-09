import csv
import os
from collections import Counter

# Loading dataset
file_path = os.path.join('Resources', 'election_data.csv') 
votes = []

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        votes.append(row[2]) 

# Calculating total number of votes cast
total_votes = len(votes)

# Calculating total number of votes each candidate won
vote_counts = Counter(votes)

# Calculating percentage of votes each candidate won
vote_percentages = {candidate: (count / total_votes) * 100 for candidate, count in vote_counts.items()}

# Who is the winner of the election based on popular vote
winner = max(vote_counts, key=vote_counts.get)

# summary
summary = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
for candidate, count in vote_counts.items():
    summary += f"{candidate}: {vote_percentages[candidate]:.3f}% ({count})\n"
summary += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------"
)


print(summary)

# Export the analysis summary to a text file
output_file_path = os.path.join('analysis', 'election_analysis.txt')
with open(output_file_path, 'w') as file:
    file.write(summary)