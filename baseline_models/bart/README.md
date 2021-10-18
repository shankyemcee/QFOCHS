# BART Model
- To finetune the BART model for query-focussed chart summarisation, we used the [summarization example code from Hugging Face](https://github.com/huggingface/transformers/tree/master/examples/pytorch/summarization)
- We finetuned the model for 2 tasks
	- Abstractive summarisation
	- Extractive summarisation

## How to Run
### Setup
1. `git clone https://github.com/huggingface/transformers`
2. `cd transformers`
3. `pip install .`
4. `pip install -r examples/pytorch/summarization/requirements.txt`
5. `cd ..`

### Abstractive Summarisation
1. `sh ./outputs_abstractive/run_bart_model.sh`

### Extractive Summarisation
1. `sh ./outputs_extractive/run_bart_model.sh`
