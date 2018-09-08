import wget
import json

def load_data():
	url = 'https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json'
	filename = wget.download(url)

	with open(filename, 'r') as f:
    	source_data = json.load(f)
    return source_data