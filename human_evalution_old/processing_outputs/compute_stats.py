import pandas as pd

df = pd.read_csv("aggregated_outputs.csv").set_index("number")
model_df = pd.read_csv("combined.csv").set_index("number")

df = pd.concat([df, model_df], axis=1)


GOLD_STANDARD = "Gold Standard"
BART = "BART"
T5 = "T5"
PAIRS = [
	(GOLD_STANDARD, BART),
	(GOLD_STANDARD, T5),
	(T5, BART),
]
CRITERIA = ["factual", "coherent", "fluent"]

df = df[~df[CRITERIA].isna().any(axis=1)]
print(len(df))

for criterion in CRITERIA:
	df.loc[:, criterion] = df[criterion]
	df[criterion] = df[criterion].astype("int")

def reverse_criterion(val):
	if val == 0:
		return 0
	elif val == 1:
		return 2
	elif val == 2:
		return 1
	else:
		raise Exception("Unknown criterion value")


for pair in PAIRS:
	pair_df_forward = df[(df["Summary 1"] == pair[0]) & (df["Summary 2"] == pair[1])].copy()
	pair_df_reversed = df[(df["Summary 1"] == pair[1]) & (df["Summary 2"] == pair[0])].copy()
	
	for criterion in CRITERIA:
		pair_df_reversed.loc[:, criterion] = pair_df_reversed[criterion].apply(reverse_criterion)

	pair_df = pd.concat([pair_df_forward, pair_df_reversed])

	print("PAIR:", pair)
	for criterion in CRITERIA:
		print(criterion)

		# Value, %
		print(pd.concat([pair_df[criterion].value_counts(), pair_df[criterion].value_counts() / len(pair_df)], axis=1).sort_index())
		print()

		# p-value
		first = len(pair_df[pair_df[criterion] == 1])
		second = len(pair_df[pair_df[criterion] == 2])
		print(first, second, first + second)

		print()

	print()

# print(df)
