# import pip_system_certs
import requests
import json
from constants.constants import cookie
import certifi


session = requests.Session()
session.verify = False


def fetch_stock_data(symbol):
    """
    Fetches the first result data for a given stock symbol from the TradingView API.

    Parameters:
    - symbol (str): The stock symbol to fetch data for.

    Returns:
    - dict: The first result data for the given stock symbol. None if no data is found.
    """
    # Base URL for the TradingView symbol search
    url = f"https://symbol-search.tradingview.com/symbol_search/v3/?text={symbol}&hl=1&exchange=&lang=en&search_type=undefined&domain=production&sort_by_country=US"

    # Headers required for the GET request
    headers = {
        'authority': 'symbol-search.tradingview.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://www.tradingview.com',
        'referer': 'https://www.tradingview.com/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }

    # Perform the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        first_result = data.get('symbols', [])[
            0] if data.get('symbols') else None
        if first_result:
            # Clean the symbol to remove HTML tags if present
            first_result['symbol'] = first_result['symbol'].replace(
                '<em>', '').replace('</em>', '')
            return first_result
    return None


def add_to_watchlist(stock_data):
    """
    Adds a list of stock symbols to the TradingView watchlist.
    """
    url = "https://www.tradingview.com/api/v1/symbols_list/custom/142620681/append/"
    payload = json.dumps([
        f"{stock_data['source_id']}:{stock_data['symbol']}"
    ])

    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'referer': 'https://www.tradingview.com/chart/4y0IIg8r/?symbol=BITSTAMP%3ABTCUSD',
    }
    response = session.post(url, headers=headers,
                            data=payload, verify=certifi.where())
    return response.json()


def remove_from_watchlist(stock_data):

    url = "https://www.tradingview.com/api/v1/symbols_list/custom/142620681/remove/"

    payload = json.dumps([
        f"{stock_data['source_id']}:{stock_data['symbol']}"
    ])

    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'referer': 'https://www.tradingview.com/chart/4y0IIg8r/?symbol=BITSTAMP%3ABTCUSD',
    }

    response = session.request(
        "POST", url, headers=headers, data=payload, verify=certifi.where())
    return response.json()
