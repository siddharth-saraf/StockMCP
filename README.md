# Stock API Service
A simple API service that retrieves stock price information using the Yahoo Finance API through a FastMCP-based API. It uses yfinance to retrieve detailed information about stocks when provided with a ticker symbol.

## Requirements
Python 3.12 or higher

## Installation

Clone this repository

### Install uv if not already installed using
```pip install uv```

### Set up a virtual environment:
```uv venv```\
```source server/.venv/bin/activate  # On Windows: server\.venv\Scripts\activate```

## Usage
To run the service:
```uv run main.py```

API Endpoints
Get Stock Info
Retrieve current stock price information:

```get_stock_info(ticker: str) -> dict```

### Parameters:
```
ticker (str): Stock ticker symbol (e.g., "AAPL" for Apple Inc.)
```
### Returns:
```
dict: A dictionary containing the following stock information:
    - symbol: Stock ticker symbol
    - shortName: Company's short name 
    - currentPrice: Current stock price
    - regularMarketChange: Price change from previous close
    - regularMarketChangePercent: Percentage change from previous close
    - regularMarketDayRange: Today's price range (low-high)
    - volume: Today's trading volume
    - marketCap: Company's market capitalization
    - fiftyTwoWeekRange: 52-week price range (low-high)
    - trailingPE: Price-to-earnings ratio (trailing 12 months)
    - dividendYield: Dividend yield as a percentage
    - sector: Company's sector
    - industry: Company's industry
    - recommendationKey: Analyst recommendations
```
Error message if the stock is not found or if an error occurs
