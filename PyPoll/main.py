import os
import csv

# Specify file path
filepath = os.path.join('Resources','election_data.csv')

# Declare variables
vote_count = 0
counts = {}
percents = {}
max_count = 0
Winner = " "

# Read csv file
with open(filepath) as csvfile:
	csvreader = csv.reader(csvfile,delimiter=',')

	csv_header = next(csvreader)

	for row in csvreader:

		vote_count += 1

		if row[2] in counts:
			counts[row[2]] += 1

		else:
			counts[row[2]] = 1
	
	for candidate,count in counts.items():
		percents[candidate] = f"{(count / vote_count) * 100:.3f}%"
		if count>max_count:
			max_count = count
			Winner = candidate
	
	#Print output to terminal
	print("Election Results")
	print("--------------------------")
	print(f"Total Votes: {vote_count}")
	print("--------------------------")
	for candidate, percent in percents.items():
		print(f"{candidate}: {percent} ({counts[candidate]})")
	print("--------------------------")
	print(f"Winner: {Winner}")
	print("--------------------------")

	# Export output to text file
	import sys
	f = open("Analysis/results.txt","a")
	sys.stdout = f				

	print("Election Results")
	print("--------------------------")
	print(f"Total Votes: {vote_count}")
	print("--------------------------")
	for candidate, percent in percents.items():
		print(f"{candidate}: {percent} ({counts[candidate]})")
	print("--------------------------")
	print(f"Winner: {Winner}")
	print("--------------------------")

	f.close()