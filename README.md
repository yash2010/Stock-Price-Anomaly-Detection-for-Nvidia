# Stock Price Anomaly Detection

This project analyzes stock price data using an LSTM-based autoencoder to detect anomalies in stock price movements. The dataset is processed, scaled, and modeled to identify significant changes in stock prices.

# Features

- Data preprocessing and scaling
- Sequence generation for time-series data
- LSTM-based autoencoder model
- Anomaly detection using reconstruction error
- Visualization of anomalies on stock price data

## Installation

```bash
pip install yfinance tensorflow pandas numpy scipy matplotlib seaborn scikit-learn
```

## Usage

**1. Prepare your dataset:**
   + Download stock data using yfinance or use a CSV file containing stock prices.
     
**2. Run the script:**
   + The main execution script processes the data, trains the model, and visualizes anomalies.
    
 **3. Example:** Modify the file_path and other configurations in the main block to your dataset.

## Folder structure:

**- DataLoader:** Handles data loading, cleaning, and sequence generation.

**- LSTMModel:** Defines and compiles the LSTM-based autoencoder.

**- Visualizer:** Contains functions for plotting reconstruction errors and anomalies.

## Workflow:
**1. Data Acquisition:** Download stock data or use an existing CSV file.

**2. Preprocessing:** Normalize the data and create sequences.

**3. Modeling:** Train an LSTM autoencoder on the training dataset.

**4. Anomaly Detection:** Identify significant changes in stock prices using reconstruction error.

**5. Visualization:** Highlight anomalies on the stock price chart.

## Example output:
### Reconstruction Error Histogram:
![output](https://github.com/user-attachments/assets/75dc7fb3-4629-41ce-9543-496c8087aca0)

### Anomaly Detection chart:
![1](https://github.com/user-attachments/assets/de0593cd-1f92-439c-bda1-087ed7a8e975)






