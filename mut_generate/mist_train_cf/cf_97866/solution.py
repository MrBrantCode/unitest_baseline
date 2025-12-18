"""
QUESTION:
Create a method in the `ArthurHayes` class that calculates the combined value of all owned cryptocurrencies and the net worth. Update the `compare_net_worth` method to compare the net worth of individuals considering their cryptocurrency investments. Introduce a new method that calculates the corresponding value of a given percentage of the individual's total net worth. The `ArthurHayes` class has attributes for name, net worth, bitcoin, ethereum, and litecoin.
"""

def calculate_combined_value(self):
    btc_price = 50000
    eth_price = 2500
    ltc_price = 200
    total_cryptocurrency_value = self.bitcoin * btc_price + self.ethereum * eth_price + self.litecoin * ltc_price
    total_value = self.net_worth + total_cryptocurrency_value
    return total_value