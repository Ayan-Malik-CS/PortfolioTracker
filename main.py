from database import get_all_stocks
from engine import get_portfolio_performance

def run_app():
    db_rows = get_all_stocks()
    
    if not db_rows:
        print("Your database is empty! Add some stocks in database.py first.")
        return

    portfolio_dict = {}
    for row in db_rows:
        ticker = row[0]
        shares = row[1]
        price = row[2]
        portfolio_dict[ticker] = (shares, price)
    
    print("--- LIVE PORTFOLIO TRACKER ---")
    get_portfolio_performance(portfolio_dict)

if __name__ == "__main__":
    run_app()