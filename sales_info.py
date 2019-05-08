import csv

with open("Sales Records.csv", "r") as csv_file_things:
    reader = csv.reader(csv_file_things)

    for row in reader:
        old_number = row[13]
        print(old_number)
