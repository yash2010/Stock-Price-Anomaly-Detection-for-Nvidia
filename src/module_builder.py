from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, RepeatVector, TimeDistributed, Dropout

class LSTMModel:
    """
    Builds and compiles an LSTM-based autoencoder model.
    Attributes:
        seq_len: int
            length of the sequence for generating time series data
    """

def __init__(self, seq_len: int):
    self.seq_len = seq_len

def build_model(self):
    """
    Returns: 
        tf.keras.Model - model: LSTM-based autoencoder model
    """
    model = Sequential([
        LSTM(128, activation='relu', input_shape=(self.seq_len, 1), return_sequences=False),
        Dropout(0.2),
        RepeatVector(self.seq_len),
        LSTM(128, activation='relu', return_sequences=True),
        TimeDistributed(Dense(1))
    ])
    model.compile(optimizer='adam', loss='mse')
    return model