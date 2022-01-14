import os
import pandas as pd

def combine_outputs(output_folder):
	output_files = os.listdir(output_folder)
	df = pd.concat([pd.read_csv(output_folder + filename) for filename in output_files if ".csv" in filename])
	df.sort_values(by="number", inplace=True)

	assert df["number"].nunique() == df["number"].count()
	print(df["number"].count())
	
	return df

df = combine_outputs("outputs/").set_index("number").sort_index()
df.to_csv("aggregated_outputs.csv")
