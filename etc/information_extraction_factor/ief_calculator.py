# -*- coding: utf-8 -*-



import json
import math

ocr_dir = "../../../bboxes/"
generated_path ="targetAnswers.txt"
reference_path = "../data/test.json"

with open(generated_path,'r',encoding='utf8') as f:
    generated = f.readlines()

with open(reference_path,'r',encoding='utf8') as f:
    test = json.load(f)



def calc_recall_ief(line_no,tokens,ocr):
    ocr_text = " ".join([key['sentence'] for key in ocr])
    ocr_text = " ".join(list(filter(lambda x: x not in fillers, set(ocr_text.split()))))
    matches=0
    if len(tokens)==0:
        return 0
    for token in tokens:
        if token.lower() in ocr_text.lower():
            matches+=1
    #return matches/len(ocr_text.split())
    return matches/len(tokens)


def calc_micro_ief(line_no,tokens,ocr):
    region_scores = []  #extraction score for each region
    weighted_region_scores = []
    lens_ = []
    for index,key in enumerate(ocr):
        counter = 0 # number of matches in each region
        for token in tokens:
            if token.lower() in key['sentence'].lower():
                counter +=1
        len_ = len(key['sentence'].split())
        if len_==0:
            print("Current ocr region empty: ", line_no)
            continue
        region_scores.append((counter/len_))
        weighted_region_scores.append((counter/len_) * math.exp(len_))
        #weighted_region_scores.append(counter)
        lens_.append(len_)
    sum_ = sum(weighted_region_scores)
    if sum_==0:
      print("Current summary extracts no ocr elements: ", line_no)
      return 0
    else:
        # normalized_region_scores = [i/sum_ for i in weighted_region_scores]
        max_ = max(weighted_region_scores)
        normalized_region_scores = [i/max_ for i in weighted_region_scores]
        
    #return max(normalized_region_scores)
    return sum(normalized_region_scores)/len(normalized_region_scores)

def calc_macro_ief(line_no,tokens,ocr):
    # ocr_text = " ".join([key['sentence'] for key in ocr])
    # ocr_text = " ".join(list(filter(lambda x: x not in fillers, set(ocr_text.split()))))
    lookup=[0]*len(ocr)
    for token in tokens:
        for index,key in enumerate(ocr):
            if token.lower() in key['sentence'].lower():
                lookup[index]=1
    return sum(lookup)/len(ocr)


fillers = ['in', 'the', 'and', 'or', 'an', 'as', 'can', 'be', 'a', ':', '-',
           'to', 'but', 'is', 'of', 'it', 'on', '.', 'at', '(', ')', ',', ';']

micro_ief=0
macro_ief=0
recall_ief=0

for index,key in enumerate(test):
    file_no = test[key][0]
    with open(ocr_dir+file_no.replace(".png",".json"),'r',encoding='utf8') as f:
        ocr = json.load(f)
    summary = generated[index]
    tokens = list(filter(lambda x: x not in fillers, set(summary.split())))
    micro_ief+=calc_micro_ief(index,tokens,ocr)
    macro_ief+=calc_macro_ief(index,tokens,ocr)
    recall_ief+=calc_recall_ief(index,tokens,ocr)

print(generated_path)
print("micro information extraction factor: ", round(micro_ief/(index+1)*100,2))
print("macro information extraction factor: ", round(macro_ief/(index+1)*100,2))
print("recall information extraction factor: ", round(recall_ief/(index+1)*100,2))







