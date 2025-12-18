"""
QUESTION:
Implement a Python class named `FinancialInstrument` that represents a financial instrument in a trading system. The class should have `symbol` and `data_source` as attributes, and include the following methods:

- `__init__(self, symbol, data_source)`: The constructor method that initializes the `symbol` and `data_source` attributes.
- `get_historical_data(self, start_date, end_date)`: A method that retrieves historical data for the instrument within the specified date range and returns a list of tuples, where each tuple contains the date and the corresponding price.
- `calculate_sma(self, period)`: A method that calculates the Simple Moving Average (SMA) for the instrument based on the specified period and returns the calculated SMA value.
- `execute_trade(self, quantity, action)`: A method that simulates executing a trade for the instrument with the specified quantity and action (buy/sell) and returns a message indicating the success of the trade execution.

Note that the methods should be implemented with placeholder logic to be replaced with actual data retrieval and trading logic.
"""

def FinancialInstrument(symbol, data_source):
    class FinancialInstrument:
        def __init__(self, symbol, data_source):
            self.symbol = symbol
            self.data_source = data_source

        def get_historical_data(self, start_date, end_date):
            # Placeholder implementation to retrieve historical data from the data source
            # Replace this with actual data retrieval logic
            historical_data = [("2022-01-01", 100.0), ("2022-01-02", 105.0), ("2022-01-03", 110.0)]
            return historical_data

        def calculate_sma(self, period):
            # Placeholder implementation to calculate Simple Moving Average
            # Replace this with actual SMA calculation logic
            sma_value = sum([price for _, price in self.get_historical_data("2022-01-01", "2022-01-03")]) / len(self.get_historical_data("2022-01-01", "2022-01-03"))
            return sma_value

        def execute_trade(self, quantity, action):
            # Placeholder implementation to simulate trade execution
            # Replace this with actual trade execution logic
            if action == "buy":
                return f"Bought {quantity} shares of {self.symbol}"
            elif action == "sell":
                return f"Sold {quantity} shares of {self.symbol}"
            else:
                return "Invalid action"
    return FinancialInstrument(symbol, data_source)