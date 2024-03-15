import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel('./stocks.xlsx')

for ticker in df['Tickers']:
    print(ticker)
