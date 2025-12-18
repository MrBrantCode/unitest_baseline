"""
QUESTION:
The function `max_profit_energy_trading` determines the optimal buying and selling strategy for a given amount of wanted energy, taking into account the market conditions and specified parameters. The function should return the maximum profit that can be achieved by buying and selling energy.

The function takes in the following parameters:
- `energy_difference`: The difference between the energy market price and the energy buy starting price.
- `energy_market_price`: The current market price of energy.
- `wanted_energy`: The amount of energy that needs to be bought or sold.
- `energy_buy_max_price`: The maximum price at which energy can be bought.
- `energy_buy_starting_price`: The initial price at which energy can be bought.
- `energy_buy_price_increment`: The increment in price for each subsequent purchase attempt.
- `energy_sell_min_price`: The minimum price at which energy can be sold.

The function should return the maximum profit as an integer.
"""

def max_profit_energy_trading(energy_difference, energy_market_price, wanted_energy, energy_buy_max_price, energy_buy_starting_price, energy_buy_price_increment, energy_sell_min_price) -> int:
    if wanted_energy <= 0:
        return 0

    if energy_market_price <= energy_buy_starting_price:
        return min(wanted_energy, energy_buy_max_price) * (energy_market_price - energy_sell_min_price)

    max_buy_price = min(energy_buy_max_price, energy_market_price + energy_difference)
    total_buy_cost = (max_buy_price + energy_buy_starting_price) * (max_buy_price - energy_buy_starting_price + energy_buy_price_increment) / (2 * energy_buy_price_increment)

    if total_buy_cost <= energy_sell_min_price * wanted_energy:
        return (max_buy_price - energy_buy_starting_price) * wanted_energy

    max_sell_price = energy_sell_min_price + energy_difference
    total_sell_profit = (energy_market_price + max_sell_price) * (max_sell_price - energy_market_price + energy_buy_price_increment) / (2 * energy_buy_price_increment)

    return total_sell_profit