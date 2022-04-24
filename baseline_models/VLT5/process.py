import csv 
import os

FOLDER_PATH = '/Users/doxuanlong/Desktop/NTUNLP/OpenCQA/QFOCHS/baseline_models/VLT5'
FILE = 'Q_OCRs_article'
T5_BASE_PATH = '/Users/doxuanlong/Desktop/NTUNLP/OpenCQA/QFOCHS/baseline_models/VLT5/T5-base.txt'

GENERATED_PATH = os.path.join(FOLDER_PATH, FILE) + '/generated.txt'
GROUND_PATH = os.path.join(FOLDER_PATH, FILE) + '/original.txt'

original_ground = []
original_generated = []

with open(GROUND_PATH) as file:
    for line in file:
        original_ground.append(line.split('\n')[0].strip())

with open(GENERATED_PATH) as file:
    for line in file:
        original_generated.append(line.split('\n')[0].strip())

assert len(original_ground) == len(original_generated)

correct_generated = []
with open(T5_BASE_PATH) as file:
    for line in file:
        t5_base = line.split('\n')[0].strip()   
        idx = original_ground.index(t5_base)
        correct_generated.append(original_generated[idx])

with open(os.path.join(FOLDER_PATH, FILE) + '/generated_predictions.txt', 'w') as file:
    for line in correct_generated:
        file.write(line)
        file.write('\n')