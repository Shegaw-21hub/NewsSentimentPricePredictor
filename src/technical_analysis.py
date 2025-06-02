import talib
import numpy as np

def calculate_ta(df):
    """Calculate technical indicators for a single stock"""
    closes = df['Close'].values
    
    # Moving Averages
    df['SMA_20'] = talib.SMA(closes, timeperiod=20)
    df['SMA_50'] = talib.SMA(closes, timeperiod=50)
    
    # RSI
    df['RSI_14'] = talib.RSI(closes, timeperiod=14)
    
    # MACD
    df['MACD'], df['MACD_Signal'], _ = talib.MACD(closes)
    
    # Bollinger Bands
    df['Upper_Band'], df['Middle_Band'], df['Lower_Band'] = talib.BBANDS(
        closes, timeperiod=20)
    
    return df

def analyze_all_stocks(stocks):
    """Apply TA to all stocks"""
    return {ticker: calculate_ta(df) for ticker, df in stocks.items()}