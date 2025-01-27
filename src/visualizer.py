import matplotlib.pyplot as plt

class Visualizer:
    """
    A class to visualize data
    """
    @staticmethod
    def plot_reconstruction_error(train_errors, test_errors):
        """
        Plots the reconstruction error

        Args:
            train_errors (list): List of training errors
            test_errors (list): List of test errors
        """
        plt.figure(figsize=(14, 8))
        plt.plot(train_errors,bins = 20, label='Train error', color='blue')
        plt.plot(test_errors, bins = 20, label='Test error', color='red')
        plt.title('Reconstruction Error')
        plt.xlabel('Error')
        plt.ylabel('Frequency')
        plt.legend()
        plt.show()
    
    @staticmethod
    def plot_anomalies(data, anomalies):
        """
        Plots anomalies on stock price data.

        Args:
           data (pd.DataFrame): Dataframe containing stock price data
           anomalies (pd.DataFrame): Dataframe containing anomalies
        """
        plt.figure(figsize=(14, 8), dpi = 150)
        plt.plot(data['Close'], color='blue', label = 'Stock price')
        plt.scatter(anomalies['Date'], anomalies['Close'], color='red', label='Anomalies')
        plt.title('Anomalies in Stock Price')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()