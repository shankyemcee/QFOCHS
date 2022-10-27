import csv 

scores = {}
scores['Gold Standard'] = []
scores['VLT5'] = []
scores['VLT5_S'] = []

idx = 2 # Factual
# idx = 3 # Relevance
# idx = 4 # Fluency

labels = []
with open('./Shankar-Others.csv') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        labels.append([
            row[11], row[12], row[13]
        ])

loop_idx = 0
with open('./Shankar-Others.csv') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        scores[labels[loop_idx][0]].append(
            int(row[idx])
        )
        scores[labels[loop_idx][1]].append(
            int(row[idx + 3])
        )
        scores[labels[loop_idx][2]].append(
            int(row[idx + 6])
        )
        loop_idx += 1

loop_idx = 0
with open('./Long-Others.csv') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        scores[labels[loop_idx][0]].append(
            int(row[idx])
        )
        scores[labels[loop_idx][1]].append(
            int(row[idx + 3])
        )
        scores[labels[loop_idx][2]].append(
            int(row[idx + 6])
        )
        loop_idx += 1

loop_idx = 0
with open('./JQ-Others.csv') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        scores[labels[loop_idx][0]].append(
            int(row[idx])
        )
        scores[labels[loop_idx][1]].append(
            int(row[idx + 3])
        )
        scores[labels[loop_idx][2]].append(
            int(row[idx + 6])
        )
        loop_idx += 1

import numpy as np
for label in scores:
    print(label, (np.asarray(scores[label]) >= 4).sum()/450)