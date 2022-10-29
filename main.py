import csv
import os

tol_tips = float(input("Total Tips = "))
tol_hrs = float(input("Total Hours = "))
num_emp = int(input("Num Employees = "))
tip_rate = tol_tips / tol_hrs
header = ["name", "hours", "tip_owd"]
tol_tips_owd = 0.0

isExist = os.path.exists('tips.csv')
if isExist:
    rowcounter = 0
    for row in open("tips.csv"):
        rowcounter += 1
    if rowcounter == num_emp + 1:
        with open("tips.csv", "r") as f:
            next(f)
            lines = f.readlines()
            writer = csv.writer(open('updated_tips.csv', 'w'))
            writer.writerow(header)
            for line in lines:
                tokens = line.split(',')
                new_hrs = float(input(f"How many hours did {tokens[0]} work? "))
                tokens[1] = new_hrs
                tokens[2] = float(tokens[1]) * tip_rate
                tokens[2] = "{:.2f}".format(tokens[2])
                tol_tips_owd = float(tol_tips_owd) + float(tokens[2])
                data = [tokens[0], tokens[1], tokens[2]]
                writer.writerow(data)
        print(tol_tips_owd)
        exit()



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
