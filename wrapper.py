import json
from keras.preprocessing import sequence
import pandas as pd
import one_hot_encoder


def wrap(input_max_length=25):
    one_hot_encoder.encode()
    file = open('full_db.json')
    db = json.load(file)
    file.close()
    file = open('words_map.json')
    words_map = json.load(file)
    file.close()
    df_x = pd.DataFrame()
    df_y = pd.DataFrame()
    names = []
    for _, x in zip(db, range(len(db))):
        print(_, x)
        data = db[_]
        names += [_] * len(data)
        encoded_data = [[words_map[word] for word in title.split()] for title in data]
        padded_data = sequence.pad_sequences(encoded_data, input_max_length)
        df_x = df_x.append(pd.DataFrame(padded_data))
    df_y['Name'] = pd.Series(names)
    df_y = pd.get_dummies(df_y)
    df_x.to_csv('X.csv', index=False)
    df_y.to_csv('y.csv', index=False)

