"""
QUESTION:
The function should be named divide_inheritance. The woman's fortune is $500,000 and she wants to divide it between her son and daughter, with the son receiving 30% less than the daughter. Write a function to calculate the amount each child receives, rounding the results to the nearest dollar.
"""

def divide_inheritance(fortune):
    """
    Calculate the amount each child receives from the woman's fortune.
    
    The daughter receives 100% of the calculated percentage and the son receives 70%.
    The total percentage is 170%.
    
    Args:
    fortune (float): The woman's fortune.
    
    Returns:
    tuple: A tuple containing the amount the daughter and son receive, respectively.
    """
    
    # Calculate 1% of the fortune
    one_percent = fortune / 170
    
    # Calculate the amount the daughter and son receive
    daughter_amount = one_percent * 100
    son_amount = one_percent * 70
    
    # Round the results to the nearest dollar
    daughter_amount = round(daughter_amount)
    son_amount = round(son_amount)
    
    return daughter_amount, son_amount