import csv 

scores = {}
scores['Gold Standard'] = []
scores['VLT5'] = []
scores['VLT5_S'] = []

idx = 2 # CS

labels = []
with open('./Shankar-CS.csv') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        labels.append([
            row[5], row[6], row[7]
        ])

loop_idx = 0
with open('./Shankar-CS.csv') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        scores[labels[loop_idx][0]].append(
            5
        )
        scores[labels[loop_idx][1]].append(
            int(row[3])
        )
        scores[labels[loop_idx][2]].append(
            int(row[4])
        )
        loop_idx += 1

loop_idx = 0
with open('./Long-CS.csv') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        scores[labels[loop_idx][0]].append(
            5
        )
        scores[labels[loop_idx][1]].append(
            int(row[3])
        )
        scores[labels[loop_idx][2]].append(
            int(row[4])
        )
        loop_idx += 1

loop_idx = 0
with open('./JQ-CS.csv') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        scores[labels[loop_idx][0]].append(
            5
        )
        scores[labels[loop_idx][1]].append(
            int(row[3])
        )
        scores[labels[loop_idx][2]].append(
            int(row[4])
        )
        loop_idx += 1

import numpy as np
for label in scores:
    print(label, (np.asarray(scores[label]) >= 4).sum()/450)

print(len(scores['VLT5']))
print(len(scores['Gold Standard']))
print(len(scores['VLT5_S']))