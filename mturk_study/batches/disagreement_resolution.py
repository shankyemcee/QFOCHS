# -*- coding: utf-8 -*-



import pandas as pd
import re


file1 = "edited_questions/output_9.csv"
file2 = "edited_questions/output_10.csv"


df1 = pd.read_csv(file1,encoding='utf8')
df2 = pd.read_csv(file2,encoding='utf8')


assert len(df1) == len(df2)

automatically_resolved_dataframe= pd.DataFrame(columns=['img_path','summary','question','answer'])
need_further_resolution1 = pd.DataFrame(columns=df1.columns)
need_further_resolution2 = pd.DataFrame(columns=df2.columns)

def calculate_score(index,row1,row2,img_path,summary,answer1,answer2,question1,question2):
    # answer1 = df1.loc[index,ans1]
    # answer2 = df2.loc[index,ans2]
    
    # question1 = df1.loc[index,ques1]
    # question2 = df2.loc[index,ques2]
    
    answer= ''
    question= ''
    global automatically_resolved_dataframe
    global need_further_resolution2
    global need_further_resolution1
    
    
    if len(answer1) > len(answer2):
        match_words = [word for word in answer2.split() if word in answer1.split()]
        match_percent = len(match_words)/len(answer2.split())
        if match_percent > 0.7 and question1 == question2: #70% of the words in the smaller sentence exists in the larger sentence and questions from both workers is same
            answer = answer1;
            question = question1
        else:
            answer = None
    
    elif len(answer2) > len(answer1):
        match_words = [word for word in answer1.split() if word in answer2.split()]
        match_percent = len(match_words)/len(answer1.split())
        if match_percent > 0.7 and question1 == question2:
            answer = answer2
            question = question2
        else:
            answer = None
    
    elif len(answer1) == len(answer2):
        if question1 == question2:
            answer = answer1
            question = question1
        else:
            answer = None
    
    

    if answer == None:
            if row1['HITId'] not in need_further_resolution1['HITId'].values:
                need_further_resolution1.loc[len(need_further_resolution1)] = row1
            
            if row2['HITId'] not in need_further_resolution2['HITId'].values:
                need_further_resolution2.loc[len(need_further_resolution2)] = row2
             
            # for img in [row1['Input.img_path4'],row1['Input.img_path5'],row1['Input.img_path6']]:
            #     if img in automatically_resolved_dataframe['img_path'].values:
            #         automatically_resolved_dataframe = automatically_resolved_dataframe[automatically_resolved_dataframe.img_path != img]

                    
    else: #if questions are equal and answers mostly equal 
            #if row1['HITId'] not in need_further_resolution1['HITId'].values and row2['HITId'] not in need_further_resolution2['HITId'].values:
                automatically_resolved_dataframe.loc[len(automatically_resolved_dataframe)] = [img_path,summary,question,answer]
                        
    
    


for index, row in df1.iterrows():
        if df1.loc[index,'Input.img_path4'] == df2.loc[index,'Input.img_path1']:
            assert df1.loc[index,'Input.summary4'] == df2.loc[index,'Input.summary1']
            img_path = df1.loc[index,'Input.img_path4']
            summary = df1.loc[index,'Input.summary4']
            ans1 = df1.loc[index,'Answer.answer4']
            ans2 = df2.loc[index,'Answer.answer1']
            ques1 = df1.loc[index,'Answer.question4']
            ques2 = df2.loc[index,'Input.question1']
            row1 = df1.iloc[index]
            row2 = df2.iloc[index]
            
            
            calculate_score(index,row1,row2,img_path,summary,ans1,ans2,ques1,ques2)
            
        if df1.loc[index,'Input.img_path5'] == df2.loc[index,'Input.img_path2']:
            
            assert df1.loc[index,'Input.summary5'] == df2.loc[index,'Input.summary2']
            img_path = df1.loc[index,'Input.img_path5']
            summary = df1.loc[index,'Input.summary5']
            ans1 = df1.loc[index,'Answer.answer5']
            ans2 = df2.loc[index,'Answer.answer2']
            ques1 = df1.loc[index,'Answer.question5']
            ques2 = df2.loc[index,'Input.question2']
            row1 = df1.iloc[index]
            row2 = df2.iloc[index]
            
            
            calculate_score(index,row1,row2,img_path,summary,ans1,ans2,ques1,ques2)
            
            
            
        if df1.loc[index,'Input.img_path6'] == df2.loc[index,'Input.img_path3']:
                    
            
            assert df1.loc[index,'Input.summary6'] == df2.loc[index,'Input.summary3']
            img_path = df1.loc[index,'Input.img_path6']
            summary = df1.loc[index,'Input.summary6']
            ans1 = df1.loc[index,'Answer.answer6']
            ans2 = df2.loc[index,'Answer.answer3']
            ques1 = df1.loc[index,'Answer.question6']
            ques2 = df2.loc[index,'Input.question3']
            row1 = df1.iloc[index]
            row2 = df2.iloc[index]
            
            calculate_score(index,row1,row2,img_path,summary,ans1,ans2,ques1,ques2)




if len(automatically_resolved_dataframe) != 0:
    automatically_resolved_dataframe.to_csv('disagreements_resolved/automatically/resolved_'+re.findall(r'\d+', file2)[0]+".csv",encoding='utf8', index=False)

if len(need_further_resolution1) != 0:
    need_further_resolution1.to_csv('unresolved_disagreements/unresolved_firsthalf_'+re.findall(r'\d+', file2)[0]+".csv",encoding='utf8', index=False)

if len(need_further_resolution2) != 0:
    need_further_resolution2.to_csv('unresolved_disagreements/unresolved_secondhalf_'+re.findall(r'\d+', file2)[0]+".csv",encoding='utf8', index=False)



  
    