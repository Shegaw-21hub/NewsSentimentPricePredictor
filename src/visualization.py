import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import gridspec
from matplotlib.patches import Patch

def plot_technical_analysis(df, ticker):
    """Generate professional TA visualization with guaranteed legend handling"""
    plt.figure(figsize=(14, 10))
    gs = gridspec.GridSpec(3, 1, height_ratios=[2, 1, 1])
    
    # --- Price Plot ---
    ax1 = plt.subplot(gs[0])
    # Explicit line creation with comma assignment
    close_line, = ax1.plot(df.index, df['Close'], label='Close', color='#1f77b4')
    sma20_line, = ax1.plot(df.index, df['SMA_20'], label='20-day SMA', color='#ff7f0e', linestyle='--')
    sma50_line, = ax1.plot(df.index, df['SMA_50'], label='50-day SMA', color='#2ca02c', linestyle='-.')
    
    # Fill between with proxy artist
    ax1.fill_between(df.index, df['Upper_Band'], df['Lower_Band'], 
                   color='gray', alpha=0.3)
    fill_proxy = Patch(facecolor='gray', alpha=0.3, label='Bollinger Bands')
    
    ax1.legend(handles=[close_line, sma20_line, sma50_line, fill_proxy])
    
    # --- RSI Plot ---
    ax2 = plt.subplot(gs[1])
    rsi_line, = ax2.plot(df.index, df['RSI_14'], label='RSI 14', color='#9467bd')
    over_line = ax2.axhline(70, color='red', linestyle='--', alpha=0.5, label='Overbought')
    under_line = ax2.axhline(30, color='green', linestyle='--', alpha=0.5, label='Oversold')
    ax2.legend(handles=[rsi_line, over_line, under_line])
    
    # --- MACD Plot ---
    ax3 = plt.subplot(gs[2])
    macd_line, = ax3.plot(df.index, df['MACD'], label='MACD', color='#17becf')
    signal_line, = ax3.plot(df.index, df['MACD_Signal'], label='Signal', color='#e377c2')
    ax3.legend(handles=[macd_line, signal_line])
    
    plt.tight_layout()
    plt.savefig(f'reports/{ticker}_technical_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()