#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os
import csv


BudgetDataCSV = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("analysis", "Budget_Output.txt")

#Set variables
TotalMonths = 0
PreviousProfit = 0
TotalProfit = []
Changes = []
Date = []

os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(BudgetDataCSV, encoding='UTF-8') as Budgetcsvfile:
    csvreader = csv.reader(Budgetcsvfile, delimiter=",")
    header = next(csvreader)

 
    for row in csvreader:
        TotalMonths += 1

        #Calculate net total of profit
        date = row[0]
        profit = (int(row[1]))

        TotalProfit.append(profit)
        Date.append(date)

        #Calculate changes in "Profit/Losses" over entire period, and then average of those changes
        #profit += (int(row[1]))
        #PreviousProfit = int(row[1])
        if TotalMonths > 1:
                change = (profit - PreviousProfit) #skip first row
                Changes.append(change) #skip first row
        PreviousProfit = profit
        
AverageChange = round(sum(Changes)/len(Changes), 2)

#Greatest increase/decrease in profits (date and amount) 
GreatestIncrease = max(Changes)
GreatestDecrease = min(Changes)
GreatestIncreaseDate = Date[Changes.index(GreatestIncrease)]
GreatestDecreaseDate = Date[Changes.index(GreatestDecrease)]

#Output into text file
output_text = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {TotalMonths}\n"
    f"Total: ${sum(TotalProfit)}\n"
    f"Average Change: ${AverageChange}\n"
    f"Greatest Increase in Profits: {GreatestIncreaseDate} (${GreatestIncrease})\n"
    f"Greatest Decrease in Profits: {GreatestDecreaseDate} (${GreatestDecrease})\n"
)

with open(OUTPUT_PATH, "w") as OutputFile:
    OutputFile.write(output_text)
    print(output_text)