import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class DataLoader:
    """
    Handles data loading and preprocessing
    Attributes:
        file_path: str
            path to the data file
        seq_len: int
            length of the sequence for generating time series data
    """
    
    def __init__(self, file_path: str, seq_len: int):
        self.file_path = file_path
        self.seq_len = seq_len
    
    def load_and_preprocessing(self):
        """
        Load data and preprocess the dataset
        Returns:
            pd.DataFrame - data: Preprocessed data
            scaler - MinMaxSclaer: Fitted scaler object
        """
        data = pd.read_csv(self.file_path)
        data = data.drop(data.index[[0,1]])
        data = data.reset_index(drop=True)
        data.rename(columns={'Unnamed: 0': 'Date'}, inplace=True)
        data['Date'] = pd.to_datetime(data['Date'])
        data.set_index('Date', inplace=True)
        df = data[['Date','Close']]
        
        scaler = MinMaxScaler(feature_range=(0, 1))
        scaled_df = scaler.fit_transform(df['Close'].values)

        return df, scaler

    def generate_sequence(self, data):
        X = []
        for i in range(len(data) - self.seq_len):
        
            X.append(data[i:(i + self.seq_len), 0])
        X = np.array(X)
        return X
    
    def calculate_pct_change(self, data, up_threshold=4, down_threshold=-4):
        """
        Calculates percentage changes in closing prices and flags significant anomalies.
        
        Args:
            data (pd.DataFrame): The preprocessed data.
            up_threshold (float): Threshold for significant upward changes.
            down_threshold (float): Threshold for significant downward changes.
        
        Returns:
            pd.DataFrame: DataFrame with additional columns for anomalies.
        """
        data['Pct_Change'] = data['Close'].pct_change() * 100
        data['Huge_Up'] = data['Pct_Change'] > up_threshold
        data['Huge_Down'] = data['Pct_Change'] < down_threshold
        anomalies = data[(data['Huge_Up'] | data['Huge_Down'])]
        return data, anomalies
    
    
    