import os
import csv
import sys

# If using relative path from main.py, use csvpath = os.path.join("..","Resources","budget_data.csv")
# If using absolute path use csvpath = os.path.join("/Users/Calvin/DS_BootCamp/Homework 3/python-challenge/PyBank/Resources/budget_data.csv")
csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # declaring and initializing variables
    num_months = 0
    total_money = 0
    total_change = 0
    avg_change = 0
    best_month = 'N/A'
    max_increase = 0
    worst_month = 'N/A'
    max_decrease = 0
    profit_change = 0
    previous_month = 0
    

    # Read each row of data after the header
    for row in csvreader:
        num_months += 1
        total_money += int(row[1])
        profit_change = int(row[1]) - previous_month

        total_change += profit_change

        if total_change > max_increase:
            best_month = (row[0])
            max_increase = profit_change
        
        if total_change < max_decrease:
            worst_month = (row[0])
            max_decrease = profit_change

        previous_month = int(row[1])

    avg_change = total_change / num_months

    # Output for terminal

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ", num_months)
    print("Total: $", total_money)
    print("Average Change: $", avg_change)
    print("Greatest Increase in Profits: ", best_month, " ($", max_increase, ")")
    print("Greatest Decrease in Profits: ", worst_month, " ($", max_decrease, ")")

    # Output for text file

    sys.stdout = open("budget_analysis.txt", "w")
    
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: ", num_months)
    print("Total: $", total_money)
    print("Average Change: $", avg_change)
    print("Greatest Increase in Profits: ", best_month, " ($", max_increase, ")")
    print("Greatest Decrease in Profits: ", worst_month, " ($", max_decrease, ")")
     
    sys.stdout.close()