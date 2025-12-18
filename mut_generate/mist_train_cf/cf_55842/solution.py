"""
QUESTION:
Create a function called `calculate_final_price` that takes three parameters: `original_price`, `tax_percentage`, and `concession_percentage`, and returns the final price of a service after adding the tax amount and applying the concession percentage. The tax amount and concession amount should be calculated as a percentage of the original price and price after tax respectively, and then added to and subtracted from the original price to get the final price.
"""

def calculate_final_price(original_price, tax_percentage, concession_percentage):
    # Calculate service tax amount
    tax_amount = original_price * (tax_percentage / 100.0)
    
    # Calculate the price after adding tax
    price_after_tax = original_price + tax_amount
    
    # Calculate the concession amount
    concession_amount = price_after_tax * (concession_percentage / 100.0)
    
    # Deduct the concession from the price
    final_price = price_after_tax - concession_amount
    
    # Return the final price
    return final_price