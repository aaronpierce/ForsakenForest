import json, os, sys

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def load(type):
	data = ''
	# with open('Entities/' + type + '.json', 'r') as f: (Before using resource_path function)
	with open(resource_path(os.path.join('Entities', (type + '.json'))), 'r') as f:
		data = json.load(f)
	return data

# Used only as a utlity to export a file to .json format to be used in game (func not used in game at all)
def to_json_format(data):
	file_name = ''
	with open(os.path.join('Entities', (file_name + '.json')), 'w+') as savefile:
		json.dump(data, savefile, indent = 4)
			
