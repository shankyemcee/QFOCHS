import pandas as pd

SAMPLE_SIZE = 150

df = pd.read_csv("test.csv")
df.sample(SAMPLE_SIZE).to_csv("test_sample.csv", index=False)
