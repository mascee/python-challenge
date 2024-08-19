#n this Challenge, you are tasked with creating a Python script to analyze the financial records
#  of your company. You will be given a financial dataset called budget_data.csv. 
# The dataset is composed of two columns: "Date" and "Profit/Losses".
#Your task is to create a Python script that analyzes the records
#  to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#Financial Analysis
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)
import os
import csv 
budget_data_csv= os.path.join("Resources", "budget_data.csv")

#Open and read csv
with open(budget_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #Skip the header
    csv_header = next(csv_file)

    #declare variables to work with data
    total_month = 0
    net_total = 0
    previous_profit_loss = None
    changes = []
    dates = []

    for row in csv_reader:
        date = row[0]
        #calculate total month
        total_month +=1
        profit_loss = int(row[1])
        #calculate net total
        net_total += profit_loss 
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
    
        previous_profit_loss = profit_loss
    
    #Calculate average change
    average_change = sum(changes)/len(changes) if changes else 0

    #Find the greates increase and decrease
    greatest_increase = max(changes) if changes else 0
    greatest_decrease = min(changes) if changes else 0
    greatest_increase_date = dates[changes.index(greatest_increase)] if changes else ""
    greatest_decrease_date = dates[changes.index(greatest_decrease)] if changes else ""

#Open PyBankAnalysis to write
analysis_txt = os.path.join("analysis", "PyBankAnalysis.txt")
with open(analysis_txt, mode='w') as txt_file:
        txt_file.write("Financial Analysis: \n")
        txt_file.write("_________________________________\n")
        txt_file.write(f"Total Month: {total_month}\n")  
        txt_file.write(f"Total: ${net_total}\n")
        txt_file.write(f"Average change: ${average_change:.2f}\n")
        txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

                       
                       



    
