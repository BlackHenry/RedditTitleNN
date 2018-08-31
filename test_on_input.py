from keras import models
from keras.preprocessing import sequence
import numpy as np
import pandas as pd
import metadata
import json
from scraper import prepare_word


def test():
    model = models.load_model('model.h5')
    user_input = prepare_word(input('Suggested title:\n'))
    print(user_input)
    file = open('words_map.json')
    words_map = json.load(file)
    file.close()
    encoded_input = [words_map[word] for word in user_input.split()]
    padded_input = sequence.pad_sequences([encoded_input], metadata.max_length)
    prediction = model.predict(np.array(padded_input))
    readable_prediction = []
    for _ in prediction[0]:
        readable_prediction.append(round(_, 3))
    prediction = readable_prediction
    num_predict = int(np.argmax(prediction))
    y = pd.read_csv('y.csv')
    for _ in range(len(prediction)):
        print(y.columns[_].replace('Name_', '') + ':', prediction[_])
    print('\n', list(y.columns)[num_predict].replace('Name_', '') + ':', prediction[num_predict])
