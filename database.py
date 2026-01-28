import sqlite3

def get_connection():
    return sqlite3.connect('portfolio.db')

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            shares REAL NOT NULL,
            purchase_price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_stock(ticker, shares, price):
    conn = get_connection()
    cursor = conn.cursor()
    
    query = "INSERT INTO stocks (ticker, shares, purchase_price) VALUES (?, ?, ?)"
    cursor.execute(query, (ticker.upper(), shares, price))
    
    conn.commit()
    conn.close()
    print(f"Added {ticker} to your database!")

def get_all_stocks():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT ticker, shares, purchase_price FROM stocks")
    rows = cursor.fetchall()
    
    conn.close()
    return rows

# Test Case
if __name__ == "__main__":
    init_db()
    
    add_stock("AAPL", 10, 150.00)
    add_stock("TSLA", 5, 200.00)
    
    data = get_all_stocks()
    print("Current Holdings in DB:", data)