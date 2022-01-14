# -*- coding: utf-8 -*-


import pandas as pd

file="../../results/run2/new3-0-99.csv"
df=pd.read_csv(file)

t5=pd.DataFrame({'factuality':[],'relevance':[],'fluency':[]})
t5_bbox=pd.DataFrame({'factuality':[],'relevance':[],'fluency':[]})
gold=pd.DataFrame({'factuality':[],'relevance':[],'fluency':[]})


#t5
t5['factuality'] = pd.concat([df.loc[df["Summary 1"]=="T5"]['factual1'],
                df.loc[df["Summary 2"]=="T5"]['factual2'],
                df.loc[df["Summary 3"]=="T5"]['factual3']])


t5['relevance'] = pd.concat([df.loc[df["Summary 1"]=="T5"]['relevant1'],
                df.loc[df["Summary 2"]=="T5"]['relevant2'],
                df.loc[df["Summary 3"]=="T5"]['relevant3']])


t5['fluency'] = pd.concat([df.loc[df["Summary 1"]=="T5"]['fluent1'],
                df.loc[df["Summary 2"]=="T5"]['fluent2'],
                df.loc[df["Summary 3"]=="T5"]['fluent3']])

#t5_bbox
t5_bbox['factuality'] = pd.concat([df.loc[df["Summary 1"]=="T5_BBOX"]['factual1'],
                df.loc[df["Summary 2"]=="T5_BBOX"]['factual2'],
                df.loc[df["Summary 3"]=="T5_BBOX"]['factual3']])


t5_bbox['relevance'] = pd.concat([df.loc[df["Summary 1"]=="T5_BBOX"]['relevant1'],
                df.loc[df["Summary 2"]=="T5_BBOX"]['relevant2'],
                df.loc[df["Summary 3"]=="T5_BBOX"]['relevant3']])


t5_bbox['fluency'] = pd.concat([df.loc[df["Summary 1"]=="T5_BBOX"]['fluent1'],
                df.loc[df["Summary 2"]=="T5_BBOX"]['fluent2'],
                df.loc[df["Summary 3"]=="T5_BBOX"]['fluent3']])

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
print("\n\n*****t5*********")
print("factuality:",(len(t5.loc[t5["factuality"]==5])+len(t5.loc[t5["factuality"]==4]))/300)
print("relevance:",(len(t5.loc[t5["relevance"]==5])+len(t5.loc[t5["relevance"]==4]))/300)
print("fluency:",(len(t5.loc[t5["fluency"]==5])+len(t5.loc[t5["fluency"]==4]))/300)



print("\n\n*****t5-bbox*********")
print("factuality:",(len(t5_bbox.loc[t5_bbox["factuality"]==5])+len(t5_bbox.loc[t5_bbox["factuality"]==4]))/300)
print("relevance:",(len(t5_bbox.loc[t5_bbox["relevance"]==5])+len(t5_bbox.loc[t5_bbox["relevance"]==4]))/300)
print("fluency:",(len(t5_bbox.loc[t5_bbox["fluency"]==5])+len(t5_bbox.loc[t5_bbox["fluency"]==4]))/300)


print("\n\n*****gold*********")
print("factuality:",(len(gold.loc[gold["factuality"]==5])+len(gold.loc[gold["factuality"]==4]))/300)
print("relevance:",(len(gold.loc[gold["relevance"]==5])+len(gold.loc[gold["relevance"]==4]))/300)
print("fluency:",(len(gold.loc[gold["fluency"]==5])+len(gold.loc[gold["fluency"]==4]))/300)



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












