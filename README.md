# Top Dividend Stock Analyzer

This Python script allows you to analyze stock performance based on total return (including dividends) over a custom date range.  
You provide a CSV file with a list of stock tickers, and the script outputs the 5 stocks with the highest total return.

---------

## Features

- Reads stock symbols from a CSV file (column header must be `Ticker`)
- Asks user to input start and end dates
- Calculates total return:  
  \[(End Price - Start Price + Total Dividends) / Start Price\]
- Prints the top 5 stocks with the highest return

------------

## Requirements

- Python 3.7+
- Packages:
  - `pandas`
  - `yfinance`

Install dependencies using:

```bash
pip install -r requirements.txt
