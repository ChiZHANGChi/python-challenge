
import csv
from statistics import mean


with open("C:/Users/craig/MonashPython/pybank/Resources/budget_data.csv", 'r') as file:
    heading = next(file)
    csvreader = csv.reader(file)

    total_months = list()
    profit_losses = list()
    changes = list()
    greatest_increase =["",0]
    greatest_decrease =["",0]

    #monthly_prof = dict()
    for row in csvreader:
        total_months.append(row[0])
        profit_losses.append(float(row[1]))
  
        if len(changes)==0:
            changes.append(0)                           
        else:
            current_change=float(row[1])-profit_losses[-2]
            changes.append(current_change)
            
            if greatest_increase[1]<current_change:
                greatest_increase[1]=current_change
                greatest_increase[0]=row[0]
                #print(greatest_increase)
            if greatest_decrease[1]>current_change:
                greatest_decrease[1]=current_change
                greatest_decrease[0]=row[0]
    #print(total_months)
    #print(profit_losses)
    #print(changes)

    print('Financial Analysis')
    print('--------------------------------')
    #print(total_months)
    print(f'Total Months:{len(total_months)}')
    print(f'Total: ${round(sum(profit_losses))}')
    print(f'Average Change: ${round(mean(changes[1:]),2)}')
    print(f'Greatest Increase in Profits:({greatest_increase[0]} ${round(max(changes))})')
    print(f'Greatest Decrease in Profits:({greatest_decrease[0]} ${round(min(changes))})')
    #print(greatest_increase[0],greatest_decrease[0])