#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os
import csv
BudgetDataCSV = os.path.join("/Users/chaunguyen/Desktop/classwork/Homework/python-challenge/PyBank/Resources/budget_data.csv")

#Set variables
TotalMonths = 0
PreviousProfit = 0
TotalProfit = []
Changes = []
Date = []


#Open csv file
with open(BudgetDataCSV, encoding='UTF-8') as Budgetcsvfile:
    csvreader = csv.reader(Budgetcsvfile, delimiter=",")

#Skip header labels
    header = next(csvreader)
# Loop 
    for row in csvreader:
#Count total months
        TotalMonths += 1

#Calculate net total of profit
        date = row[0]
        profit = (int(row[1]))
        TotalProfit.append(profit)
        Date.append(date)

#Calculate changes in "Profit/Losses" over entire period, and then average of those changes
        change = (profit - PreviousProfit)
        Changes.append(change)
        PreviousProfit = profit
        AverageChange = sum(Changes)/(TotalMonths)

#Greatest increase/decrease in profits (date and amount) 
GreatestIncrease = max(Changes)
GreatestDecrease = min(Changes)
GreatestIncreaseDate = Date[Changes.index(GreatestIncrease)]
GreatestDecreaseDate = Date[Changes.index(GreatestDecrease)]

#Output into text file
#OutputPath = os.path.join("..", "analysis", "Bank_Data_Output.txt")

Output = os.path.join("Pybank", "analysis", "Budget_Output.txt")

with open(Output, "w") as OutputFile:
    OutputFile.write("Financial Analysis\n")
    OutputFile.write("----------------------------\n")
    OutputFile.write(f"Total Months: {TotalMonths}\n")
    OutputFile.write(f"Total: ${sum(TotalProfit)}\n")
    OutputFile.write(f"Average Change: ${AverageChange}\n")
    OutputFile.write(f"Greatest Increase in Profits: {GreatestIncreaseDate} (${GreatestIncrease})\n")
    OutputFile.write(f"Greatest Decrease in Profits: {GreatestDecreaseDate} (${GreatestDecrease})\n")