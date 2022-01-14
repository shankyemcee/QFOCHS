import pandas as pd
import shutil

test_images = list(pd.read_csv("test_sample.csv")["image_no"])

for img in test_images:
	shutil.copy(f"../../../QFOCHS_dataset/chart_images/{img}", f"images/{img}")
