import csv

file = open("data.csv", "r")
content = csv.reader(file)

for row in content:
    print(row)

file.close()