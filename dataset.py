import csv

categories = {}
with open('Dataset.csv', mode='r') as file:
    reader = csv.reader(file, delimiter=']')
    for row in reader:
        if len(row) > 1:
            categories[int(row[0].strip('['))] = row[1].strip()

responses = {}
with open('Database.csv', mode='r') as file:
    reader = csv.reader(file, delimiter=']')
    for row in reader:
        if len(row) > 1:
            category = int(row[0].strip('['))
            if category not in responses:
                responses[category] = []
            responses[category].append(row[1].strip())