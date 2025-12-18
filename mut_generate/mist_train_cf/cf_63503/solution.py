"""
QUESTION:
Design a function `gain_forward_volatility_exposure` that calculates the forward volatility exposure using the given at-the-money (ATM) volatilities for two different expiration dates, and returns the calculated forward volatility exposure. The function should take the following parameters: `short_term_volatility`, `long_term_volatility`, `short_term_time_to_expiration`, and `long_term_time_to_expiration`. The function should return the calculated forward volatility exposure.
"""

def gain_forward_volatility_exposure(short_term_volatility, long_term_volatility, short_term_time_to_expiration, long_term_time_to_expiration):
    forward_volatility_exposure = ((long_term_time_to_expiration * long_term_volatility) - (short_term_time_to_expiration * short_term_volatility)) / (long_term_time_to_expiration - short_term_time_to_expiration)
    return forward_volatility_exposure