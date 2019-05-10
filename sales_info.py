import csv

with open("Sales Records.csv", "r") as csv_file_things:
    reader = csv.reader(csv_file_things)
    total = 0
    for row in reader:
        profit = row[13]
        category = row[2]
        if category == "Fruits":
            print(profit, category)
            total += float(profit)
    print(total)
