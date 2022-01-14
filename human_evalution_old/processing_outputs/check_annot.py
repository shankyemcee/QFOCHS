"""
check_annot.py: Checks which chart numbers you have completely annotated according to the output folder.
"""

import os
import pandas as pd

output_files = os.listdir("outputs/")
nums = set()

for filename in output_files:
	if ".csv" in filename:
		nums = nums.union(list(pd.read_csv("outputs/" + filename)["number"]))

def display_num_list(ls):
	if len(ls) == 0:
		return ""

	output = ""

	start_num = ls[0]
	prev_num = ls[0]
	for num in ls[1:]:
		if num - prev_num == 1:
			prev_num = num
			continue
		else:
			if start_num != prev_num:
				output += f"{start_num}-{prev_num}, "
			else:
				output += f"{start_num}, "
			
			start_num = num
			prev_num = num

	if start_num != prev_num:
		output += f"{start_num}-{prev_num}"
	else:
		output += f"{start_num}"

	return output

nums = sorted(list(nums))
print(display_num_list(nums))
