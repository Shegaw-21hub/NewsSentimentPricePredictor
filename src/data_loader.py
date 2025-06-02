import pandas as pd
import glob

def load_all_stocks(data_path='data/*_historical_data.csv'):
    """Load all stock CSV files into a dictionary of DataFrames"""
    files = glob.glob(data_path)
    stocks = {}
    
    for file in files:
        ticker = file.split('_')[0].split('/')[-1]  # Extract ticker from filename
        df = pd.read_csv(file, parse_dates=['Date'], index_col='Date')
        df.rename(columns={'Adj Close': 'Adj_Close'}, inplace=True)
        stocks[ticker] = df[['Open', 'High', 'Low', 'Close', 'Volume']]  # Select required columns
        
    return stocks