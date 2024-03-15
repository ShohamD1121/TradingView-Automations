from utils.utils import fetch_stock_data, add_to_watchlist
from time import sleep
import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('stocks.xlsx')

stocks_to_insert = []

for stock in df['Tickers']:
    stocks_to_insert.append(stock)

for stock in stocks_to_insert:
    stock_data = fetch_stock_data(stock)
    print(stock_data)
    if stock_data:
        print(f"Adding {stock_data['symbol']} to watchlist...")
        result = add_to_watchlist(stock_data)
    else:
        print(f"No data found for {stock}")
    sleep(0.5)
