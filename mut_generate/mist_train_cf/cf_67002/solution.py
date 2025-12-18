"""
QUESTION:
Write a function named `calculate_dv01` that takes the fixed rate of a plain vanilla interest rate swap as input and returns the corresponding DV01 value, which represents the change in the value of the swap for a 1 basis point (0.01%) movement in yield. Assume that the swap has a fixed notional amount.
"""

def calculate_dv01(fixed_rate):
    # Assuming a fixed notional amount of $100
    notional_amount = 100
    
    # Calculate the present value of a 1 basis point (0.01%) movement in yield
    # This is a simplified example and actual calculation may involve more complex financial modeling
    dv01 = notional_amount * 0.0001
    
    return dv01