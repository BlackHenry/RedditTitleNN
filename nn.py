from keras.models import Sequential
from keras.layers import LSTM, Dense, Embedding, Flatten
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import metadata


def train(frac=0.8, embedding_vector_size=20, lstm_size=300, batch_size=32, epochs=20):
    x_data = pd.read_csv('X.csv')
    y_data = pd.read_csv('y.csv')
    random_state = int(np.random.rand(1) * 100)
    train_x = x_data.sample(frac=frac, random_state=random_state)
    test_x = x_data.iloc[x_data.index.difference(train_x.index)]
    train_y = y_data.sample(frac=frac, random_state=random_state)
    test_y = y_data.iloc[y_data.index.difference(train_y.index)]
    m_l = metadata.max_length
    model = Sequential()
    model.add(Embedding(metadata.vocab_size + 1, embedding_vector_size, input_length=m_l))
    # model.add(LSTM(lstm_size))
    model.add(Flatten())
    model.add(Dense(y_data.shape[1], activation='softmax'))
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

    history = model.fit(train_x, train_y, batch_size=batch_size, epochs=epochs)
    model.save('model.h5')
    results = model.evaluate(test_x, test_y)
    print(results)
    prediction = model.predict(test_x)
    test_y.to_csv('true_y.csv')
    pd.DataFrame(prediction).to_csv('pred_y.csv')
    plt.plot(history.history['categorical_accuracy'])
    plt.show()


