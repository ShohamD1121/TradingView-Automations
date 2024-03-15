from utils.utils import fetch_stock_data, remove_from_watchlist
from time import sleep

stocks_to_remove = ["SPY", "QQQ"]
                   
for stock in stocks_to_remove:
    stock_data = fetch_stock_data(stock)
    if stock_data:
        print(f"Removing {stock_data['symbol']} from watchlist...")
        result = remove_from_watchlist(stock_data)
    else:
        print(f"No data found for {stock}")
    sleep(0.5)