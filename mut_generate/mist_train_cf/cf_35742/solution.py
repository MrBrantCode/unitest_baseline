"""
QUESTION:
Create a function `calculate_pnl` that calculates the break-even point and potential profit or loss for options trading. The function should take in five parameters: `put` (a boolean indicating whether the option is a put option), `strike` (the strike price), `sell_factor` (the factor by which the premium is reduced when selling the option), `premium` (the premium paid for the option), and `price_at_expiry` (the price of the underlying asset at the option's expiry). The function should return a tuple containing the break-even point and the potential profit or loss.
"""

def calculate_pnl(put: bool, strike: float, sell_factor: float, premium: float, price_at_expiry: float) -> (float, float):
    if put:
        break_even = strike - sell_factor * premium
        pnl = strike - premium - price_at_expiry
    else:
        break_even = strike + sell_factor * premium
        pnl = premium - strike + price_at_expiry
    return break_even, pnl