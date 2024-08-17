<div>
  <img src="https://raw.githubusercontent.com/GeorgeTelles/georgetelles/f69531ec6b293b5148563588a764c010015d315e/logo_clara.png" alt="logo clara" width="300" style="display: inline-block; vertical-align: top; margin-right: 10px;">
  <img src="https://raw.githubusercontent.com/GeorgeTelles/georgetelles/f69531ec6b293b5148563588a764c010015d315e/logo_dark.png" alt="logo dark" width="300" style="display: inline-block; vertical-align: top;">
</div>

# Profit vs. Return Banks

## Description

This project is an investment model that evaluates the relationship between bank profits and their growth on the stock exchange. In other words, the goal is to determine whether the bank that made the most profit also experienced the greatest increase in stock market value. The analysis is conducted using historical stock price data and bank profit data.

## Features

- **Data Collection**: Uses the `yfinance` library to fetch adjusted closing prices for major Brazilian banks and the Ibovespa index from January 2010 to August 2023.
- **Return Calculation**: Computes the percentage return for bank stocks and the Ibovespa index based on the adjusted stock prices at the beginning and end of the period.
- **Profit Analysis**: Compares the percentage growth in bank profits over the same period.
- **Visualization**: Generates graphs displaying the returns of bank stocks and profit growth, allowing for a clear visual comparison.

## Libraries Used

- `pandas`: Data manipulation and analysis.
- `yfinance`: Downloading historical stock data.
- `pandas_datareader`: For financial data reading (mentioned as a dependency but not used directly in the current code).
- `matplotlib`: Creating graphs for data visualization.

