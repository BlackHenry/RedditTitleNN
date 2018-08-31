import json


max_length = 25
file = open('words_map.json')
vocab_size = len(json.load(file))
file.close()
