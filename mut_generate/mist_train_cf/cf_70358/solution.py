"""
QUESTION:
Scale Bond Yields for Visualization 

Write a function `scale_bond_yields` that scales bond yields to visualize its relative impact to asset valuations. The function should take a list of bond yields and the initial yield value as input, and return a list of scaled yields that represent the percentage change from the initial yield. The scaled yields should be calculated by dividing each yield by the initial yield value and subtracting 1. 

Restrictions: Assume a constant equity risk premium and EPS.
"""

def scale_bond_yields(bond_yields, initial_yield):
    """
    This function scales bond yields to visualize its relative impact to asset valuations.
    
    Args:
        bond_yields (list): A list of bond yields.
        initial_yield (float): The initial yield value.
    
    Returns:
        list: A list of scaled yields that represent the percentage change from the initial yield.
    """
    # Calculate the scaled yields by dividing each yield by the initial yield value and subtracting 1
    scaled_yields = [(yield_value / initial_yield) - 1 for yield_value in bond_yields]
    
    return scaled_yields