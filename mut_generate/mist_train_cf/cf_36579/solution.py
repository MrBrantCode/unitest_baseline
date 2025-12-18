"""
QUESTION:
Create a function `generateStockHeader(stock_data)` that takes a list of stock data as input and returns a formatted header string with the following columns: 
- "Id" - Stock identifier
- "Name" - Stock name
- "Current" - Current stock price
- "MA6 %" - 6-day moving average percentage change
- "MA10 %" - 10-day moving average percentage change
- "1 month" - Percentage change over 1 month
- "3 months" - Percentage change over 3 months
- "6 months" - Percentage change over 6 months
- "1 year" - Percentage change over 1 year
- "1/3/6/12" - Combined percentage change over 1 month, 3 months, 6 months, and 1 year.
"""

def generateStockHeader(stock_data):
    header_format = '{:>10}{:>32}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}'
    header = header_format.format("Id", "Name", "Current", "MA6 %", "MA10 %", "1 month", "3 months", "6 months", "1 year", "1/3/6/12")
    return header