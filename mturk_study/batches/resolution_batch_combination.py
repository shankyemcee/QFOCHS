# -*- coding: utf-8 -*-



import pandas as pd
import re

#original files
file1 = "edited_answers/user_split_remaining/Tiffany/pair1/output_27.csv"
file2 = "edited_answers/user_split_remaining/Tiffany/pair1/output_28.csv"

output_dir = "disagreements_resolved/combined_final/batch_27.csv"

file_resolved_batches = ["disagreements_resolved/manually_remaining/Tiffany/pair1/batch_27(0-99).csv"
                           ]

df1 = pd.read_csv(file1,encoding='utf8')
df2 = pd.read_csv(file2,encoding='utf8')

df_resolved = pd.read_csv(file_resolved_batches[0],encoding='utf8')

assert len(df1) == len(df2)

combined_output = pd.DataFrame(columns=df_resolved.columns)
combined_output['title'] = []
combined_output['original_answer'] = [] 

               

def find_extra_info(img,answer_resolution,extractive_answer):
        if len(df1.loc[df1['Input.img_path4'] == img]) != 0:
            title = df1.loc[df1['Input.img_path4'] == img]['Input.title4'].values[0]
            if answer_resolution=='same' or answer_resolution=='answer1':
                original_answer = df1.loc[df1['Input.img_path4'] == img]['Answer.answer4'].values[0]
            elif answer_resolution=='answer2':
                original_answer = df2.loc[df2['Input.img_path1'] == img]['Answer.answer1'].values[0]
            elif answer_resolution=='new_answer':
                original_answer = extractive_answer
            
        elif len(df1.loc[df1['Input.img_path5'] == img]) != 0:
            title = df1.loc[df1['Input.img_path5'] == img]['Input.title5'].values[0]
            if answer_resolution=='same' or answer_resolution=='answer1':
                original_answer = df1.loc[df1['Input.img_path5'] == img]['Answer.answer5'].values[0]
            elif answer_resolution=='answer2':
                original_answer = df2.loc[df2['Input.img_path2'] == img]['Answer.answer2'].values[0]
            elif answer_resolution=='new_answer':
                original_answer = extractive_answer
        
        elif len(df1.loc[df1['Input.img_path6'] == img]) != 0:
            title = df1.loc[df1['Input.img_path6'] == img]['Input.title6'].values[0]
            if answer_resolution=='same' or answer_resolution=='answer1':
                original_answer = df1.loc[df1['Input.img_path6'] == img]['Answer.answer6'].values[0]
            elif answer_resolution=='answer2':
                original_answer = df2.loc[df2['Input.img_path3'] == img]['Answer.answer3'].values[0]
            elif answer_resolution=='new_answer':
                original_answer = extractive_answer
        else:
            raise Exception("Could not find image",img)
        
        return title, original_answer





for file in file_resolved_batches:
    df_resolved = pd.read_csv(file,encoding='utf8')
    for index, row in df_resolved.iterrows():
        title, original_answer = find_extra_info(row['img_path'],row['answer_resolution'],row['extractive_answer'])
        # combined_output.loc[-1] = pd.concat([row, pd.Series([title,original_answer],index=['title','original_answer'])], axis=0)
        combined_output.loc[-1] = row       #if title and original_answer is available in the csv
        combined_output.index = combined_output.index + 1
        combined_output = combined_output.sort_index()



combined_output.to_csv(output_dir,encoding='utf8', index=False)







    