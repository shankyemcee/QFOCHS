# -*- coding: utf-8 -*-


import pandas as pd

file="../../results/vlt5/output_full.csv"
df=pd.read_csv(file)

t5=pd.DataFrame({'factuality':[],'relevance':[],'fluency':[]})
t5_bbox=pd.DataFrame({'factuality':[],'relevance':[],'fluency':[]})
gold=pd.DataFrame({'factuality':[],'relevance':[],'fluency':[]})


#t5
t5['factuality'] = pd.concat([df.loc[df["Summary 1"]=="VLT5"]['factual1'],
                df.loc[df["Summary 2"]=="VLT5"]['factual2'],
                df.loc[df["Summary 3"]=="VLT5"]['factual3']])


t5['relevance'] = pd.concat([df.loc[df["Summary 1"]=="VLT5"]['relevant1'],
                df.loc[df["Summary 2"]=="VLT5"]['relevant2'],
                df.loc[df["Summary 3"]=="VLT5"]['relevant3']])


t5['fluency'] = pd.concat([df.loc[df["Summary 1"]=="VLT5"]['fluent1'],
                df.loc[df["Summary 2"]=="VLT5"]['fluent2'],
                df.loc[df["Summary 3"]=="VLT5"]['fluent3']])

#t5_bbox
t5_bbox['factuality'] = pd.concat([df.loc[df["Summary 1"]=="VLT5_S"]['factual1'],
                df.loc[df["Summary 2"]=="VLT5_S"]['factual2'],
                df.loc[df["Summary 3"]=="VLT5_S"]['factual3']])


t5_bbox['relevance'] = pd.concat([df.loc[df["Summary 1"]=="VLT5_S"]['relevant1'],
                df.loc[df["Summary 2"]=="VLT5_S"]['relevant2'],
                df.loc[df["Summary 3"]=="VLT5_S"]['relevant3']])


t5_bbox['fluency'] = pd.concat([df.loc[df["Summary 1"]=="VLT5_S"]['fluent1'],
                df.loc[df["Summary 2"]=="VLT5_S"]['fluent2'],
                df.loc[df["Summary 3"]=="VLT5_S"]['fluent3']])

#gold
gold['factuality'] = pd.concat([df.loc[df["Summary 1"]=="Gold Standard"]['factual1'],
                df.loc[df["Summary 2"]=="Gold Standard"]['factual2'],
                df.loc[df["Summary 3"]=="Gold Standard"]['factual3']])


gold['relevance'] = pd.concat([df.loc[df["Summary 1"]=="Gold Standard"]['relevant1'],
                df.loc[df["Summary 2"]=="Gold Standard"]['relevant2'],
                df.loc[df["Summary 3"]=="Gold Standard"]['relevant3']])


gold['fluency'] = pd.concat([df.loc[df["Summary 1"]=="Gold Standard"]['fluent1'],
                df.loc[df["Summary 2"]=="Gold Standard"]['fluent2'],
                df.loc[df["Summary 3"]=="Gold Standard"]['fluent3']])

print(file)

#Only matching rating 4,5 on likert scale
print("\n\n*****vlt5*********")
print("factuality:",(len(t5.loc[t5["factuality"]==5])+len(t5.loc[t5["factuality"]==4]))/150)
print("relevance:",(len(t5.loc[t5["relevance"]==5])+len(t5.loc[t5["relevance"]==4]))/150)
print("fluency:",(len(t5.loc[t5["fluency"]==5])+len(t5.loc[t5["fluency"]==4]))/150)



print("\n\n*****vlt5_S*********")
print("factuality:",(len(t5_bbox.loc[t5_bbox["factuality"]==5])+len(t5_bbox.loc[t5_bbox["factuality"]==4]))/150)
print("relevance:",(len(t5_bbox.loc[t5_bbox["relevance"]==5])+len(t5_bbox.loc[t5_bbox["relevance"]==4]))/150)
print("fluency:",(len(t5_bbox.loc[t5_bbox["fluency"]==5])+len(t5_bbox.loc[t5_bbox["fluency"]==4]))/150)


print("\n\n*****gold*********")
print("factuality:",(len(gold.loc[gold["factuality"]==5])+len(gold.loc[gold["factuality"]==4]))/150)
print("relevance:",(len(gold.loc[gold["relevance"]==5])+len(gold.loc[gold["relevance"]==4]))/150)
print("fluency:",(len(gold.loc[gold["fluency"]==5])+len(gold.loc[gold["fluency"]==4]))/150)



#Only matching rating 5 on likert scale
# print("\n\n*****t5*********")
# print("factuality:",(len(t5.loc[t5["factuality"]==5]))/300)
# print("relevance:",(len(t5.loc[t5["relevance"]==5]))/300)
# print("fluency:",(len(t5.loc[t5["fluency"]==5]))/300)



# print("\n\n*****t5-bbox*********")
# print("factuality:",(len(t5_bbox.loc[t5_bbox["factuality"]==5]))/300)
# print("relevance:",(len(t5_bbox.loc[t5_bbox["relevance"]==5]))/300)
# print("fluency:",(len(t5_bbox.loc[t5_bbox["fluency"]==5]))/300)


# print("\n\n*****gold*********")
# print("factuality:",(len(gold.loc[gold["factuality"]==5]))/300)
# print("relevance:",(len(gold.loc[gold["relevance"]==5]))/300)
# print("fluency:",(len(gold.loc[gold["fluency"]==5]))/300)












