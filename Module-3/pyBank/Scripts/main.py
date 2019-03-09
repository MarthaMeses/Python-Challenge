#Unit 3 Assigment - Py Me Up, Charlie
#pyBank: Financial Analysis
#@version 1.0
#@author Martha Meses

import os
import csv

filePath = "../Resources/budget_data.csv"

totalRows = 0
totalMonths = 0
totalProfitLosses = 0
budget_data_dic = {}
budget_data_Date = []
budget_data_PL= []
averageChange = 0
indexDateMax = 0
indexDateMin = 0
greatestDecreaseProfits = 0
greatestIncreaseProfits = 0

with open(filePath, "r") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        if totalRows == 0:
             #First row is the headers 
             #budget_data_dic = {", ".join(row)}
             #print(budget_data_dic)
             totalRows += 1
        #budget_data_dic = {row["Date"],row["Profit/Losses"]}
        
        budget_data_PL.append(int(row["Profit/Losses"]))
        budget_data_Date.append(row["Date"])
        totalMonths += 1
        totalProfitLosses += int(row["Profit/Losses"])
        totalRows += 1
    csvFile.close()

averageChange = float(totalProfitLosses/totalMonths)
greatestIncreaseProfits = max(budget_data_PL)
indexDateMax = budget_data_PL.index(greatestIncreaseProfits)
greatestDecreaseProfits = min(budget_data_PL)
indexDateMin = budget_data_PL.index(greatestDecreaseProfits)
print("\nFINANCIAL ANALYSIS\n")
print("------------------\n\n")
#print(f'Processed {totalRows} lines.')
print(f'Total Months:    {totalMonths}\n')
print(f'Total:           ${totalProfitLosses:,}\n')
print(f'Average Change:  {averageChange:.2f}\n')
print(f'Greatest Increase in Profits: {budget_data_Date[indexDateMax]} (${greatestIncreaseProfits})\n')
print(f'Greatest Decrease in Profits: {budget_data_Date[indexDateMin]} (${greatestDecreaseProfits})\n')

writeResultsFile = open("../Resources/financialAnalysisResults.txt", "w")  
writeResultsFile.write("FINANCIAL ANALYSIS\n") 
writeResultsFile.write("------------------\n\n")
writeResultsFile.write(f'Total Months:    {totalMonths}\n')
writeResultsFile.write(f'Total:           ${totalProfitLosses:,}\n')
writeResultsFile.write(f'Average Change:  {averageChange:.2f}\n')
writeResultsFile.write(f'Greatest Increase in Profits: {budget_data_Date[indexDateMax]} (${greatestIncreaseProfits})\n')
writeResultsFile.write(f'Greatest Decrease in Profits: {budget_data_Date[indexDateMin]} (${greatestDecreaseProfits})\n')
writeResultsFile.close() 
