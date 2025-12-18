"""
QUESTION:
Create a function `calculate_net_cost` that calculates the net price of a product given its base cost, discount percentage, regional tax rate, and membership status. The function should first apply the discount to the base cost, then apply an additional 5% discount if the user is a member, and finally add the regional tax rate to the cost. The discount percentages and tax rate should be provided as percentages.
"""

def calculate_net_cost(base_cost, discount_percentage, tax_rate, is_member):
    """
    This function calculates the net price of a product.
    
    :param base_cost: Initial cost of the product.
    :param discount_percentage: Discount on the product given as a percentage.
    :param tax_rate: The regional tax rate given as a percentage.
    :param is_member: A boolean indicating whether the user is a member (which gives additional discounts).
    :return: The net cost of the product after applying the discounts and adding the tax. 
    """
    
    # calculate the cost after applying the discount
    net_cost = base_cost * (1 - discount_percentage/100)
    
    # if the user is a member, apply an additional 5% discount
    if is_member:
        net_cost = net_cost * (1 - 5/100)
        
    # now apply the regional tax rate
    net_cost = net_cost * (1 + tax_rate/100)
    
    return net_cost