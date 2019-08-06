import os
import csv

def total(previous, change):
    total = previous + change
    return total


def greatest_increase(current, new):
    if (int(new[1]) > int(current[1])):
        return new
    else:
        return current


def greatest_decrease(current, new):
    if (int(new[1]) < int(current[1])):
        return new
    else:
        return current


csv_path = os.path.join("Resources", "budget_data.csv")

write_path = os.path.join("Resources", "Analysis.txt")

ttl = 0
grtest_inc = ["", 0]
grtest_dec = ["", 0]
average_change = 0
number_months = 0
#-------------------------------
with open(csv_path, newline = '') as csv_file:
    
    csv_reader = csv.reader(csv_file, delimiter = ",")
    
    header = next(csv_reader)
    
    for row in csv_reader:
        number_months += 1
        grtest_inc = greatest_increase(grtest_inc, row)
        grtest_dec = greatest_decrease(grtest_dec, row)
        ttl = total(ttl, int(row[1]))
#------------------------------
average_change = ttl/number_months
    
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {number_months}")
print(f"Total Profit: ${ttl}")
print(f"Greatest Increase: {grtest_inc[0]}, ${grtest_inc[1]}")
print(f"Greatest Decrease: {grtest_dec[0]}, ${grtest_dec[1]}")
print(f"Average Change: ${average_change:.2f}")
#--------------------------------
with open(write_path, "w") as file1:
    file1.write("Financial Analysis\n")
    file1.write("-------------------------\n")
    file1.write(f"Total Months: {number_months}\n")
    file1.write(f"Total Profit: ${ttl}\n")
    file1.write(f"Greatest Increase: {grtest_inc[0]}, ${grtest_inc[1]}\n")
    file1.write(f"Greatest Decrease: {grtest_dec[0]}, ${grtest_dec[1]}\n")
    file1.write(f"Average Change: ${average_change:.2f}\n")
#-------------------------------------


