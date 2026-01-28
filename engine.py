import yfinance as yf

def get_portfolio_performance(holdings):
    
    print(f"{'Ticker':<10} | {'Price':<10} | {'Gain/Loss %':<12} | {'Total Value'}")
    print("-" * 50)
    
    total_portfolio_value = 0
    
    for ticker_symbol, (shares, buy_price) in holdings.items():
        try:
            ticker = yf.Ticker(ticker_symbol)
            # Fetch current price
            current_price = ticker.info.get("currentPrice") or ticker.info.get("regularMarketPrice")
            
            if current_price:
                # Calculations
                current_value = shares * current_price
                total_portfolio_value += current_value
                
                # Gain/Loss Percentage formula: ((Current - Buy) / Buy) * 100
                percent_change = ((current_price - buy_price) / buy_price) * 100
                
                print(f"{ticker_symbol:<10} | ${current_price:<9.2f} | {percent_change:>10.2f}% | ${current_value:>10.2f}")
            else:
                print(f"{ticker_symbol:<10} | Price data unavailable")
                
        except Exception as e:
            print(f"Error fetching {ticker_symbol}: {e}")

    print("-" * 50)
    print(f"Total Portfolio Value: ${total_portfolio_value:,.2f}")

if __name__ == "__main__":
    # Mock data representing your current holdings
    # Format: "TICKER": (Shares, Avg Buy Price)
    my_test_portfolio = {
        "AAPL": (5, 175.50),
        "GOOGL": (2, 140.00),
        "TSLA": (10, 210.00)
    }
    
    get_portfolio_performance(my_test_portfolio)