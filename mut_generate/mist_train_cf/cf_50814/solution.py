"""
QUESTION:
Write a function `delta_hedge_swaption` that calculates the notional amount of a swap required to delta hedge a swaption. The swaption has a given notional amount, expiry, and underlying swap with a given maturity. The function should take in the notional amount of the swaption, the delta of the swaption, and the expiry and maturity of the underlying swap as inputs, and return the required notional amount of the swap.
"""

def delta_hedge_swaption(notional_swaption, delta_swaption, expiry_swaption, maturity_underlying_swap):
    return notional_swaption * delta_swaption