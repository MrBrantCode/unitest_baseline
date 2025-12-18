"""
QUESTION:
Create a function `compute_discount` that takes two parameters: `cost` and `discount_rate` (defaulting to 0.15), calculates the final amount after applying the discount, and returns it. Ensure the function handles non-numeric and negative inputs by returning an error message if either condition is met.
"""

def compute_discount(cost, discount_rate=0.15):
    try:
        cost = float(cost)
        discount_rate = float(discount_rate)
        if cost < 0 or discount_rate < 0:
            return 'Error: Negative values are not accepted'
        else:
            final_amount = cost - (cost * discount_rate)
            return final_amount
    except ValueError:
        return 'Error: Input must be a number'