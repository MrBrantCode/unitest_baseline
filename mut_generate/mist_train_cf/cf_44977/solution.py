"""
QUESTION:
Create a function `calculate_differential_cost` that takes the following parameters: 
- the number of units sold per year 
- the annual revenue 
- the annual variable cost 
- the annual fixed cost 
- the cost of the new equipment 
- the annual depreciation of the new equipment 
- the sale price of the old equipment 
- the number of years the new equipment is amortized over 

Calculate the differential cost between using the old equipment and the new equipment.
"""

def calculate_differential_cost(units_sold, annual_revenue, annual_variable_cost, annual_fixed_cost, new_equipment_cost, annual_depreciation, old_equipment_sale_price, amortization_years):
    """
    Calculate the differential cost between using the old equipment and the new equipment.

    Args:
    units_sold (int): The number of units sold per year.
    annual_revenue (float): The annual revenue.
    annual_variable_cost (float): The annual variable cost.
    annual_fixed_cost (float): The annual fixed cost.
    new_equipment_cost (float): The cost of the new equipment.
    annual_depreciation (float): The annual depreciation of the new equipment.
    old_equipment_sale_price (float): The sale price of the old equipment.
    amortization_years (int): The number of years the new equipment is amortized over.

    Returns:
    float: The differential cost.
    """

    # Calculate earnings with old equipment
    earnings_old = annual_revenue - annual_variable_cost - annual_fixed_cost
    
    # Calculate earnings with new equipment
    new_equipment_annual_cost = (new_equipment_cost - old_equipment_sale_price) / amortization_years
    earnings_new = annual_revenue - annual_variable_cost - annual_fixed_cost - new_equipment_annual_cost + annual_depreciation
    
    # Calculate differential cost
    differential_cost = earnings_old - earnings_new
    
    return differential_cost