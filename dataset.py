import csv

categories = {}
with open('Dataset.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 2:
            number, category = row
            categories[int(number)] = category.strip()

responses = {}
with open('Database.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 2:
            number, sentence = row
            responses[int(number)] = sentence.strip()