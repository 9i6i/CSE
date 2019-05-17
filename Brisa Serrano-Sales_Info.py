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
        if category == "Meat":
            print(profit, category)
            total += float(profit)
        if category == "Clothes":
            print(profit, category)
            total += float(profit)
        if category == "Baby Food":
            print(profit, category)
            total += float(profit)
        if category == "Vegetables":
            print(profit, category)
            total += float(profit)
        if category == "Beverages":
            print(profit, category)
            total += float(profit)
        if category == "Cereal":
            print(profit, category)
            total += float(profit)
        if category == "Cosmetics":
            print(profit, category)
            total += float(profit)
        if category == "Household":
            print(profit, category)
            total += float(profit)
        if category == "Office Supplies":
            print(profit, category)
            total += float(profit)
        if category == "Personal Care":
            print(profit, category)
            total += float(profit)
        if category == "Snacks":
            print(profit, category)
            total += float(profit)
    print(total)
