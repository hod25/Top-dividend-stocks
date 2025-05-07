import pandas as pd
import yfinance as yf
from datetime import datetime

# Load the CSV file with stock tickers (first row should be a header, e.g., "Ticker")
file_path = input("Enter the path to the CSV file (or just its name if it's in the same folder): ")
df = pd.read_csv(file_path)

# Make sure there's a column named "Ticker"
if "Ticker" not in df.columns:
    raise ValueError("The file must contain a column named 'Ticker' with stock symbols.")

tickers = df["Ticker"].dropna().unique()

# Get date input
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")

# Validate date format
try:
    datetime.strptime(start_date, "%Y-%m-%d")
    datetime.strptime(end_date, "%Y-%m-%d")
except ValueError:
    raise ValueError("Invalid date format. Use YYYY-MM-DD.")

# Processing
data = []

for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(start=start_date, end=end_date)

        if hist.empty:
            continue

        start_price = hist['Close'][0]
        end_price = hist['Close'][-1]
        dividends = hist['Dividends'].sum()

        total_return = (end_price - start_price + dividends) / start_price
        data.append((ticker, total_return))
    except Exception as e:
        print(f"Error processing {ticker}: {e}")

# Sort by return
top_5 = sorted(data, key=lambda x: x[1], reverse=True)[:5]

print("\nTop 5 stocks with the highest total return:")
for ticker, ret in top_5:
    print(f"{ticker}: {ret:.2%}")
