from flask import Flask, render_template, request, redirect, url_for
from database import get_all_stocks, add_stock
import yfinance as yf

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # If the user clicks "Buy Stock" (Submit button)
    if request.method == 'POST':
        ticker = request.form['ticker']
        shares = float(request.form['shares'])
        price = float(request.form['price'])
        
        # Save it to your Phase 2 Database
        add_stock(ticker, shares, price)
        
        # Refresh the page to show the new stock
        return redirect(url_for('index'))

    # Regular loading of the dashboard
    db_data = get_all_stocks()
    portfolio = []
    total_val = 0
    
    for row in db_data:
        stock_id, ticker_symbol, shares, buy_price = row
        ticker = yf.Ticker(ticker_symbol)
        curr_price = ticker.info.get("currentPrice") or ticker.info.get("regularMarketPrice")
        
        if curr_price:
            total_stock_val = shares * curr_price
            total_val += total_stock_val
            gain_loss = ((curr_price - buy_price) / buy_price) * 100
            
            portfolio.append({
                'id': row[0],
                'ticker': ticker_symbol,
                'shares': shares,
                'price': f"${curr_price:.2f}",
                'gain_loss': f"{gain_loss:.2f}%",
                'total': f"${total_stock_val:.2f}"
            })

    return render_template('index.html', portfolio=portfolio, total_val=f"{total_val:.2f}")

from database import get_all_stocks, add_stock, delete_stock # Add delete_stock to imports

@app.route('/delete/<int:stock_id>')
def delete(stock_id):
    delete_stock(stock_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)