import pandas as pd
import random

GOLD_STANDARD = "Gold Standard"
T5_BBOX = "T5_BBOX"
T5 = "T5"
PAIRS = [
	(GOLD_STANDARD, T5_BBOX, T5),
	(GOLD_STANDARD, T5, T5_BBOX),
	(T5, GOLD_STANDARD, T5_BBOX),
    (T5, T5_BBOX, GOLD_STANDARD),
    (T5_BBOX, T5, GOLD_STANDARD),
    (T5_BBOX, GOLD_STANDARD, T5)
    
]

output_files = {
	T5_BBOX: "t5_bbox(without_summary)/t5-bbox.txt",
	T5: "t5_with_summary/t5.txt",
}

df = pd.read_csv("../dataset/test_sample.csv")
SAMPLE_SIZE = len(df)

# Metadata
df["Gold Standard"] = df["abstractive_answer"].apply(lambda x: x.strip())
df["title"] = df["title"].apply(lambda x: x.strip())
df["question"] = df["question"].apply(lambda x: x.strip())
df["img"] = df["image_no"].apply(lambda x: "dataset/images/" + x)
df = df[["id", "title", "question", "img", "Gold Standard"]]

# Model outputs
original_df = pd.read_csv("../dataset/test.csv",encoding='utf8').set_index("id")

for name, filename in output_files.items():
	with open(filename) as f:
		original_df[name] = f.read().split("\n")

df = pd.concat([
	df.set_index("id"),
	original_df.loc[df["id"], list(output_files.keys())]
], axis=1)

df = pd.concat([df] * 6)

# Assign summaries
assignments = []

for pair in PAIRS:
	for i in range(SAMPLE_SIZE):
		if bool(random.getrandbits(1)):
			assignments.append(pair)
		else:
			assignments.append(tuple(reversed(pair)))

df["Summary 1"] = list(map(lambda x: x[0], assignments))
df["Summary 2"] = list(map(lambda x: x[1], assignments))
df["Summary 3"] = list(map(lambda x: x[2], assignments))

df = df.sample(frac=1)
df.reset_index(inplace=True)
df.index.rename("number", inplace=True)
df.to_csv("combined.csv")
