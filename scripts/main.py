from src.data_loader import load_all_stocks
from src.technical_analysis import analyze_all_stocks
from src.visualization import plot_technical_analysis
import pynance as pn
import pandas as pd
import os

def calculate_financial_metrics(stocks):
    """Calculate PyNance metrics for all stocks"""
    metrics = []
    
    for ticker, df in stocks.items():
        returns = pn.returns(df['Close'])
        metrics.append({
            'Ticker': ticker,
            'Annual_Return': pn.annualized_return(returns),
            'Annual_Volatility': pn.annualized_volatility(returns),
            'Sharpe_Ratio': pn.sharpe_ratio(returns),
            'Max_Drawdown': pn.max_drawdown(df['Close'])
        })
    
    return pd.DataFrame(metrics)

def main():
    # Create reports directory
    os.makedirs('reports', exist_ok=True)
    
    # Load and analyze data
    stocks = load_all_stocks()
    analyzed_stocks = analyze_all_stocks(stocks)
    
    # Generate visualizations
    for ticker, df in analyzed_stocks.items():
        plot_technical_analysis(df, ticker)
    
    # Calculate financial metrics
    metrics_df = calculate_financial_metrics(analyzed_stocks)
    metrics_df.to_csv('reports/financial_metrics.csv', index=False)
    
    print("✅ Analysis complete! Check the reports/ directory.")

if __name__ == "__main__":
    main()