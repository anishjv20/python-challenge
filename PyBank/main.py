import os

import csv

budget_data = os.path.join('Resources','budget_data.csv')

total_months = 0

total_sum = 0

total_sum2 = 0

initial_value = 0

initial_value1 = 0

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
			difference = int(row[2])
			
			if initial_value1 == 0:
				initial_value1 = int(row[2])
			
			else:
				if initial_value1 < int(row[2]):
					min_value = initial_value1
					initial_value1 = int(row[2])
					min_date = row[0]
				else:
					max_value = initial_value1
					initial_value1 = int(row[2])
					max_date = row[0]
				
		average_change = total_sum2/total_months
		
	print("Financial Analysis")
	print("--------------------")
	print(f"Total months: {total_months}")
	print(f"Total sum: {total_sum}")
	print(f"total change: {total_sum2}")
	print(f"Average change: ${average_change}")
	print(f"Greatest increase in profits: {max_date} (${max_value})")
	print(f"Greatest decrease in profits: {min_date} (${min_value})")
