import os

def load_data(path):
	"""
	Load dataset
	"""
	print("loading dataset")
	input_file = os.path.join(path)
	with open(input_file, "r", encoding='utf8') as f:
		data = f.read()

	return data.split('\n')
