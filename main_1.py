import os
import csv


file_csv = "PyBank_Resources_budget.csv"
file_txt = "Resources_budget_data.txt"


total_months = 1
preve_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 1]
total_revenue = 0

with open(file_csv) as revenue_data:
    csv_file = csv.DictReader(revenue_data)
    first_row = next(csv_file)
    total_revenue += int(first_row["Profit/Losses"])
    preve_revenue += int(first_row["Profit/Losses"])

    for line in csv_file:

        # Total
        total_months = total_months + 1
        total_revenue = total_revenue + int(line["Profit/Losses"])

        # The average
        revenue_change = int(line["Profit/Losses"]) - preve_revenue
        preve_revenue = int(line["Profit/Losses"])
        revenue_change_list += [revenue_change]
        month_of_change += [line["Date"]]

        # The greatest increase
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = line["Date"]
            greatest_increase[1] = revenue_change

        #The greatest  decrease
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = line["Date"]
            greatest_decrease[1] = revenue_change

# Claculate the average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

Total = (
    f"\nFinancial Analysis\n"
    f"--------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_revenue}\n"
    f"Average Change: ${(round(revenue_avg, 2))}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[1]} (${greatest_decrease[1]})\n")

print(Total)


with open(file_txt, "w") as txt_file:
    txt_file.write(Total)
