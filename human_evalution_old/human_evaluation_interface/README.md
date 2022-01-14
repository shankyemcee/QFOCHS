# Human Evaluation
## Generating New Test Sample
1. `cd dataset/`
2. `python sample_test_index.py`
3. `python copy_images.py`
	1. May need to adjust the folder location on line 7 based on where the images files are	

## Generating Model Output Files
1. Add model files to `outputs/` folder
2. `cd outputs/`
3. `python generate_csv.py` 
	1. May need to adjust the lines 5 to 16 based on the model outputs used & the pairwise comparisons

## Running the Evaluation Interface
- You need to host the `index.html` file as a server so that it can load the csv files
- A simple way is provided below
- You can host the website on Heroku or any other platform, so that other people can access it without having to host it themselves

###
1. Install [Node.js](https://nodejs.org/en/)
2. `npx live-server .`
