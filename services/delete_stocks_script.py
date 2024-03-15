from utils.utils import fetch_stock_data, remove_from_watchlist
from time import sleep
import pandas as pd

def read_stocks_from_excel(file_path):
    """
    Reads stock tickers from an Excel file into a list.

    :param file_path: Path to the Excel file.
    :return: List of stock tickers.
    """
    df = pd.read_excel(file_path)
    return df['Tickers'].tolist()

def remove_stocks_from_watchlist(stocks):
    """
    Processes each stock by fetching its data and adding it to the watchlist.

    :param stocks: List of stock tickers.
    """
    for stock in stocks:
        stock_data = fetch_stock_data(stock)
        if stock_data:
            print(f"Removing {stock_data['symbol']} from watchlist...")
            remove_from_watchlist(stock_data)
        else:
            print(f"No data found for {stock}")
        sleep(1)