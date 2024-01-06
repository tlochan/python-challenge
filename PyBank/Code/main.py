import os 
import csv

#bankcsv set = to filepath for input csv
bankcsv = os.path.join("..", "Resources" , "budget_data.csv")

#open the file as myfile in readmode
with open(bankcsv, 'r', newline="") as myfile:
        #begin reading the csv
        reader = csv.reader(myfile,delimiter=",")
        
        #reading, storing, and skipping past the headers
        headers = next(reader)
        
        #variables and lists for following tasks
        month = []
        year = []
        monthly_profit = []
        totalprofit = 0
        max_date_index = 0
        min_date_index = 0
        
        #for loop which looks at the data in each column
        for row in reader:
         splitdate = row[0].split("-")
         month.append(splitdate[0])
         year.append(splitdate[1])
         
         #total profit keeps a running sum
         totalprofit = totalprofit + int(row[1])
         monthly_profit.append(int(row[1]))
        
        #outside the forloop, find the max and min in the list 
        maxprofit = max(monthly_profit)
        minprofit = min(monthly_profit)
        
        #for loop looking to create a variable to store the index of the max/min profit months
        for x in monthly_profit:
            if x == maxprofit:
                max_date_index = monthly_profit.index(x)
            if x == minprofit:
               min_date_index = monthly_profit.index(x) 
        
        #total months as the length of the number of months - omits header row
        total_months = len(month)
        average_profit = round((totalprofit/total_months),2)
        
        #printing data on console
        print("Financial Analysis")
        print("------------------------------------------------")
        print("Total months: " + str(total_months))
        print("Total profit: $" + str(totalprofit))
        print("Average profit per month: $" +str(average_profit))
        print("Greatest profit in a month: $" + str(maxprofit) + " in " + str(month[max_date_index]) + " 20" + str(year[max_date_index]))
        print("Largest loss in a month: $" + str(minprofit)+ " in " + str(month[min_date_index]) + " 20" + str(year[min_date_index]))

output = os.path.join("..", "Analysis", "Financial_Analysis.txt")

with open(output, 'w', newline="") as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(["Financial Analysis"])
        writer.writerow(["------------------------------------------------"])
        writer.writerow(["Total months: " + str(total_months)])
        writer.writerow(["Total profit: $" + str(totalprofit)])
        writer.writerow(["Average profit per month: $" +str(average_profit)])
        writer.writerow(["Greatest profit in a month: $" + str(maxprofit) + " in " + str(month[max_date_index]) + " 20" + str(year[max_date_index])])
        writer.writerow(["Largest loss in a month: $" + str(minprofit)+ " in " + str(month[min_date_index]) + " 20" + str(year[min_date_index])])