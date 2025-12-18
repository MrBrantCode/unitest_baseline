"""
QUESTION:
Create a function `checkNeutralFinancialValue` that takes four parameters: `value`, `currency`, `exchangeRate`, and `inflationRate`. The function should calculate the adjusted value of `value` based on `exchangeRate` and `inflationRate`, and return `True` if the adjusted value is neither a financial gain nor a loss (i.e., equals 0), and `False` otherwise. Assume that the exchange rate and inflation rate are static values, and do not account for real-time financial data.
"""

def checkNeutralFinancialValue(value, currency, exchangeRate, inflationRate):
    # Calculate the adjusted value based on the inflation rate and the exchange rate.
    adjustedValue = (value * exchangeRate) / (1 + inflationRate)

    # Check if the adjusted value is neither a gain nor a loss.
    return adjustedValue == 0