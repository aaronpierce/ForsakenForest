import json

def load(type):
	data = ''
	with open('GameEntities/' + type + '.json', 'r') as f:
		data = json.load(f)
	return data
