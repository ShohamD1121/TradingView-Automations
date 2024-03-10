from utils.utils import fetch_stock_data, add_to_watchlist
from time import sleep

stocks_to_insert = ["SPY", "QQQ"]

for stock in stocks_to_insert:
    stock_data = fetch_stock_data(stock)
    if stock_data:
        print(f"Adding {stock_data['symbol']} to watchlist...")
        result = add_to_watchlist(stock_data)
    else:
        print(f"No data found for {stock}")
    sleep(0.5)
