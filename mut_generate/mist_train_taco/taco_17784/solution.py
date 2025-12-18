"""
QUESTION:
Create a function that returns the total of a meal including tip and tax. You should not tip on the tax.

You will be given the subtotal, the tax as a percentage and the tip as a percentage. Please round your result to two decimal places.
"""

def calculate_meal_total(subtotal, tax_percentage, tip_percentage):
    # Calculate the tax amount
    tax_amount = subtotal * (tax_percentage / 100.0)
    
    # Calculate the total after adding tax
    total_with_tax = subtotal + tax_amount
    
    # Calculate the tip amount based on the subtotal (not including tax)
    tip_amount = subtotal * (tip_percentage / 100.0)
    
    # Calculate the final total including tip
    final_total = total_with_tax + tip_amount
    
    # Round the result to two decimal places
    return round(final_total, 2)