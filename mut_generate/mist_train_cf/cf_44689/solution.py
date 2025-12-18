"""
QUESTION:
Compute the FX Delta Risk of a bond. The bond's face value (Notional), Trade Price, and the currency in which the bond pays coupons are known. The FX Rate from the bond's currency to USD is also given. The function should calculate the FX Delta Risk given a small change in the foreign exchange rate.
"""

def compute_fx_delta_risk(notional, trade_price, fx_rate):
    # Assuming a simple linear relationship for demonstration purposes.
    # In a real-world scenario, this computation would likely involve more complex calculations.
    dv_df = trade_price  # derivative of bond price with respect to FX rate
    fx_delta_risk = notional * dv_df
    return fx_delta_risk