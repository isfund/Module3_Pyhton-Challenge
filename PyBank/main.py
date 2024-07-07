import csv

# loading the budget_data.csv
file_path = r'C:\Module3_Python-Challenge\PyBank\Resources\budget_data.csv'
dates = []
profits_losses = []

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        dates.append(row[0])
        profits_losses.append(int(row[1]))

# Total number of months
total_months = len(dates)

# Calculate the net total amount of "Profit/Losses" over the entire timespan
net_total = sum(profits_losses)

# Calculate the changes in "Profit/Losses" over the timespan
changes = [profits_losses[i] - profits_losses[i - 1] for i in range(1, len(profits_losses))]
average_change = sum(changes) / len(changes)

# id greatest increase in profits (date and amount)
greatest_increase = max(changes)
greatest_increase_date = dates[changes.index(greatest_increase) + 1]

# id greatest decrease in profits (date and amount)
greatest_decrease = min(changes)
greatest_decrease_date = dates[changes.index(greatest_decrease) + 1]

# summary
summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:.2f})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:.2f})"
)


print(summary)

# Export of summary to a text file
output_file_path = r'C:\Module3_Python-Challenge\PyBank\analysis\financial_analysis.txt' 
with open(output_file_path, 'w') as file:
    file.write(summary)