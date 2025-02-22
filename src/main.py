from data_loader import DataLoader
from module_builder import LSTMModel
from visualizer import Visualizer
import numpy as np
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    # Configs
    file_path = 'data/NVDA.csv'
    seq_len = 50
    theshold_percentile = 95
    
    #Load and preprocess data
    loader = DataLoader(file_path, seq_len)
    data, scaler = loader.load_and_preprocessing()
    sequences = loader.generate_sequences(data)

    # Calculates percentage change and anomalies
    data, anomalies = loader.calculate_percentage_change(data, up_threshold = 4, down_threshold = -4)

    # Split data into train and test
    X_train, X_test = train_test_split(X, test_size=0.3, shuffle=False)
    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1) 

    # Build model
    model_builder = LSTMModel(seq_len)
    model = model_builder.build_model()
    model.fit(X_train, X_train, epochs=20, batch_size=8, validation_data=(X_test, X_test))
    
    # Model Evaluation and Visualization
    reconst_test = model.predict(X_test)
    test_errors = np.mean(np.abs(reconst_test - X_test), axis=(1,2))
    thresh = np.percentile(test_errors, theshold_percentile)
    anomalies = data.iloc[len(X_train):][test_errors > thresh]

    Visualizer.plot_anomalies(test_errors[:len(X_test)], test_errors[len(X_train):])
    Visualizer.plot_anomalies(data, anomalies)
