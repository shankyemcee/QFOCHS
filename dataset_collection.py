# -*- coding: utf-8 -*-




# from sklearn import utils
import os
import pandas as pd
import shutil
import json
from sklearn import utils
import re

dataset = {}
target_image_path = "chart_images/"
source_image_path = "../chart2text_extended/c2t_dataset_pew(not_complete)/out/"
full_dataset_target_path = "data/full_dataset.json"
train_dataset_target_path = "data/train.json"
test_dataset_target_path = "data/test.json"
val_dataset_target_path = "data/val.json"

target_bbox_path = "bboxes/"
source_bbox_path = "../chart2text_extended/c2t_dataset_pew/dataset/"
#metadata for no_data folder and root out folder
out_multicol_metadata = pd.read_csv("../chart2text_extended/c2t_dataset_pew/dataset/multiColumn/metadata.csv",encoding='utf8')
out_twocol_metadata = pd.read_csv("../chart2text_extended/c2t_dataset_pew/dataset/metadata.csv",encoding='utf8')


#metadata for no_data_remaining folder
remain_multicol_metadata = pd.read_csv(source_image_path + "no_data_remaining/multi_col/metadata.csv",encoding='utf8')
remain_twocol_metadata = pd.read_csv(source_image_path + "no_data_remaining/two_col/metadata.csv",encoding='utf8')





#keep adding to the list when new batches are resolved and ready
batch_list = ["DQA/mturk_study/batches/disagreements_resolved/combined/batch_11.csv"]

combined_frame = pd.DataFrame()

for batch in batch_list:
    combined_frame = pd.concat([combined_frame,pd.read_csv(batch)])
    
combined_frame.reset_index(drop=True, inplace=True)



combined_frame.to_csv("all_annotations.csv",encoding='utf8')

counter=0


def find_bbox_path(source_image,img_no):
    
    if "out/no_data/multi_col" in source_image:
        row = out_multicol_metadata[ out_multicol_metadata['old_id'] == 'no_data-'+img_no[:len('.png')]]
        if len(row) == 0:
            row = out_twocol_metadata[ out_twocol_metadata['old_id'] == 'no_data-'+img_no[:len('.png')]]
        bbox_path = row['bboxesPath'].item()
    elif "out/no_data/two_col" in source_image:
        row = out_twocol_metadata[ out_twocol_metadata['old_id'] == 'no_data-'+img_no[:len('.png')]]
        if len(row) == 0:
            row = out_multicol_metadata[ out_multicol_metadata['old_id'] == 'no_data-'+img_no[:len('.png')]]
        bbox_path = row['bboxesPath'].item()
    elif "out/multi_col" in source_image:
        row = out_multicol_metadata[ out_multicol_metadata['old_id'] == 'multi_col-'+img_no[:len('.png')]]
        if len(row) == 0:
            row = out_twocol_metadata[ out_twocol_metadata['old_id'] == 'two_col-'+img_no[:len('.png')]]
        bbox_path = row['bboxesPath'].item()
    elif "out/two_col" in source_image:
        row = out_twocol_metadata[ out_twocol_metadata['old_id'] == 'two_col-'+img_no[:len('.png')]]
        if len(row) == 0:
            row = out_multicol_metadata[ out_multicol_metadata['old_id'] == 'multi_col-'+img_no[:len('.png')]]
        bbox_path = row['bboxesPath'].item()
    elif "out/no_data_remaining/multi_col" in source_image:
        old_id = remain_multicol_metadata[ remain_multicol_metadata['id'] == int(img_no[:len('.png')])]['old_id'].item()
        row = out_multicol_metadata[ out_multicol_metadata['old_id'] == old_id]
        if len(row) == 0:
            row = out_twocol_metadata[ out_twocol_metadata['old_id'] == old_id]
        bbox_path = row['bboxesPath'].item()
    elif "out/no_data_remaining/two_col" in source_image:
        old_id = remain_twocol_metadata[ remain_twocol_metadata['id'] == int(img_no[:len('.png')])]['old_id'].item()
        row = out_twocol_metadata[ out_twocol_metadata['old_id'] == old_id]
        if len(row) == 0:
            row = out_multicol_metadata[ out_multicol_metadata['old_id'] == old_id]
        bbox_path = row['bboxesPath'].item()
    
    return bbox_path







for index,row in combined_frame.iterrows():
    relative_path = row['img_path'][len('mturk_charts/'):row['img_path'].rfind('/')+1] + "imgs/"
    img_no = row['img_path'][row['img_path'].rfind('/')+1:]
    source_image = source_image_path + relative_path + img_no
    target_image = target_image_path + str(counter) + ".png"
    shutil.copy(source_image,target_image)
    
    bbox_path = find_bbox_path(source_image,img_no)
    source_bbox = source_bbox_path + bbox_path
    target_bbox = target_bbox_path + str(counter) + ".json"
    shutil.copy(source_bbox,target_bbox)
    
    
    dataset[counter] =  [
                         str(counter)+".png",
                         row['title'],
                         row['summary'],
                         row['question'],
                         row['abstractive_answer'],
                         row['extractive_answer']
                         ]
    
    counter+=1






with open(full_dataset_target_path, 'w', encoding='utf8') as f:
    json.dump(dataset, f)



# shuffle data with seed=0 for reproducibility
indicesShuffled = utils.shuffle(list(dataset.keys()) , random_state=0)

trainSize = round(len(indicesShuffled) * 0.7)
testSize = round(len(indicesShuffled) * 0.15)
validSize = len(indicesShuffled) - trainSize - testSize


train_data = {}
val_data = {}
test_data = {}


for file_no in range(0,trainSize):
    train_data[indicesShuffled[file_no]] = dataset[indicesShuffled[file_no]]


for file_no in range(trainSize,trainSize + validSize):
    val_data[indicesShuffled[file_no]] = dataset[indicesShuffled[file_no]]


for file_no in range(trainSize + validSize,len(indicesShuffled)):
    test_data[indicesShuffled[file_no]] = dataset[indicesShuffled[file_no]]


with open(train_dataset_target_path, 'w', encoding='utf8') as f:
    json.dump(train_data, f)

with open(val_dataset_target_path, 'w', encoding='utf8') as f:
    json.dump(val_data, f)

with open(test_dataset_target_path, 'w', encoding='utf8') as f:
    json.dump(test_data, f)





