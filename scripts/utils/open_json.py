import json
def open_json(file):
    with open(file, 'r') as config_file:
        return json.load(config_file)