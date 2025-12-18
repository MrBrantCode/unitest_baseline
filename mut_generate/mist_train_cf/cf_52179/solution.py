"""
QUESTION:
Write a function called `calculate_net_price` that takes five parameters: the base cost of a product, the discount percentage, the federal tax rate, the state tax rate, and a boolean indicating whether it's a holiday sale. The function should return the net price of the product considering the given rates and conditions. If the product is on holiday sale, an additional 5% discount should be applied. The function should handle invalid inputs (negative numbers and non-numeric data types) and return an error message. The time complexity should not exceed O(n).
"""

def calculate_net_price(base_cost, discount_percent, federal_tax_rate, state_tax_rate, holiday_sale):
    try:
        if base_cost<0 or discount_percent<0 or federal_tax_rate<0 or state_tax_rate<0:
            return 'Error: All inputs must be non-negative!'
        
        if holiday_sale == True:
            additional_discount = 0.05  # assuming 5% additional discount on holiday sales
            discount_percent += additional_discount
            if discount_percent>1:
                discount_percent = 1
        
        initial_price = base_cost - (base_cost*discount_percent)
        
        net_price = initial_price + (initial_price*federal_tax_rate) + (initial_price*state_tax_rate)
        
        return round(net_price, 2)
    
    except TypeError:
        return 'Error: Invalid input data type!'