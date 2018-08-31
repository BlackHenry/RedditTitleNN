import json
import pandas as pd


words_map = {}
vocab_size = 0


def encode():
    global words_map, vocab_size
    file = open('full_db.json')
    db = json.load(file)
    file.close()
    all_words = []
    for _, i in zip(db, range(len(db))):
        print(_, i)
        for title in db[_]:
            all_words += title.split()
    all_words = list(set(all_words))
    print(len(all_words))
    all_words = pd.Series(all_words)
    words_map = pd.DataFrame()
    words_map['Words'] = all_words
    words_map['Encoding'] = pd.Series(words_map.index) + 1
    vocab_size = words_map.shape[0]
    print(vocab_size)
    words_map = words_map.set_index('Words').to_dict('index')
    for _ in words_map:
        words_map[_] = words_map[_]['Encoding']
    file = open('words_map.json', 'w')
    json.dump(words_map, file)
    file.close()
