import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import gridspec

def plot_technical_analysis(df, ticker):
    """Generate professional TA visualization with proper legend handling"""
    plt.figure(figsize=(14, 10))
    gs = gridspec.GridSpec(3, 1, height_ratios=[2, 1, 1])
    
    # Price and Moving Averages
    ax1 = plt.subplot(gs[0])
    line_close = ax1.plot(df.index, df['Close'], label='Close', color='#1f77b4')
    line_sma20 = ax1.plot(df.index, df['SMA_20'], label='20-day SMA', color='#ff7f0e', linestyle='--')
    line_sma50 = ax1.plot(df.index, df['SMA_50'], label='50-day SMA', color='#2ca02c', linestyle='-.')
    band_fill = ax1.fill_between(df.index, df['Upper_Band'], df['Lower_Band'], 
                               color='gray', alpha=0.3, label='Bollinger Bands')
    
    # Explicit legend creation with handles
    ax1.legend(handles=[
        line_close[0], 
        line_sma20[0], 
        line_sma50[0],
        plt.Rectangle((0,0), 1, 1, fc='gray', alpha=0.3)  # For fill_between
    ])
    
    # RSI Plot
    ax2 = plt.subplot(gs[1])
    line_rsi = ax2.plot(df.index, df['RSI_14'], label='RSI 14', color='#9467bd')
    line_overbought = ax2.axhline(70, color='red', linestyle='--', alpha=0.5, label='Overbought')
    line_oversold = ax2.axhline(30, color='green', linestyle='--', alpha=0.5, label='Oversold')
    ax2.legend()
    
    # MACD Plot
    ax3 = plt.subplot(gs[2])
    line_macd = ax3.plot(df.index, df['MACD'], label='MACD', color='#17becf')
    line_signal = ax3.plot(df.index, df['MACD_Signal'], label='Signal', color='#e377c2')
    ax3.legend()
    
    plt.tight_layout()
    plt.savefig(f'reports/{ticker}_technical_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()