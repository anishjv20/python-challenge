import os
import csv

# Specify file path
budget_data = os.path.join('Resources','budget_data.csv')

#Declare variables
total_months = 0

total_sum = 0

total_sum2 = 0

initial_value = 0

initial_value1 = 0

initial_value2 = 0

# Read csv file
with open(budget_data) as csvfile:
	csvreader = csv.reader(csvfile,delimiter=',')

	csv_header = next(csvreader)

	for row in csvreader:
		total_months += 1
		total_sum += int(row[1])
		
		if (initial_value == 0):
			
			initial_value = int(row[1])
			
		else:
			
			difference = int(row[1]) - initial_value
			total_sum2 = total_sum2 + difference
			initial_value = int(row[1])
			
			if initial_value1 == 0:
				initial_value1 = difference
			
			elif initial_value1 < difference:
				min_value = initial_value1
				
			else:
				min_value = difference
				initial_value1 = min_value
			
				if initial_value1 == min_value:
					min_date = row[0]		
			
			if initial_value2 == 0:
				initial_value2 = difference
			
			elif initial_value2 > difference:
				max_value = initial_value2
				
			else:
				max_value = difference
				initial_value2 = max_value

				if initial_value2 == max_value:
					max_date = row[0]
					
		average_change = total_sum2/total_months
		
	# Print output to terminal
	print("Financial Analysis")
	print("--------------------")
	print(f"Total months: {total_months}")
	print(f"Total sum: {total_sum}")
	print(f"Total change: {total_sum2}")
	print(f"Average change: ${average_change}")
	print(f"Greatest increase in profits: {max_date} (${max_value})")
	print(f"Greatest decrease in profits: {min_date} (${min_value})")

	# Export output to text file
	import sys
	f = open("Analysis/results.txt","a")
	sys.stdout = f				
	
	print("Financial Analysis")
	print("--------------------")
	print(f"Total months: {total_months}")
	print(f"Total sum: {total_sum}")
	print(f"Total change: {total_sum2}")
	print(f"Average change: ${average_change}")
	print(f"Greatest increase in profits: {max_date} (${max_value})")
	print(f"Greatest decrease in profits: {min_date} (${min_value})")
	
	f.close()

