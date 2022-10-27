import csv
import os
import pandas

tol_tips = float(input("Total Tips = "))
tol_hrs = float(input("Total Hours = "))
num_emp = int(input("Num Employees = "))
tip_rate = tol_tips / tol_hrs

isExist = os.path.exists('tips.csv')
if isExist:
    rowcounter = 0
    for row in open("tips.csv"):
        rowcounter += 1
    if rowcounter == num_emp + 1:
        with open("tips.csv", 'r+') as f:
            reader = csv.DictReader(f)
            for row in reader:
                new_hrs = float(input(f"How many hours did {row['name']} work? "))
                row['hours'] = new_hrs
                row['tip_owd'] = row['hours'] / tip_rate
        exit()

header = ["name", "hours", "tip_owd"]

with open("tips.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(num_emp):
        name = str(input(f"Employee {i + 1} Name = "))
        hrs = float(input("Hours Worked = "))
        tip_owd = hrs * tip_rate
        tip_owd = round(tip_owd, 2)
        data = [name, hrs, tip_owd]
        writer.writerow(data)
