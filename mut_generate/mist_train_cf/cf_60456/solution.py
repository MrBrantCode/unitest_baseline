"""
QUESTION:
Create a function `calculate_total_amount` that calculates the total amount in a bank account after a certain number of years, considering annual interest and contributions. The function should take four arguments: `years`, `principle`, `annual_rate`, and `contributions`, representing the total years, initial deposit amount, annual rate of interest, and annual deposit amount, respectively. The function should return the total amount after the specified years. If any errors occur during the calculation, the function should return the error message.
"""

def calculate_total_amount(years, principle, annual_rate, contributions):
    """
    A function to calculate the total amount in your bank account after a certain number of years
    
    Args:
        years (int): total years
        principle (float): your initial deposit amount 
        annual_rate (float): the annual rate of interest provided by the bank 
        contributions (float): annual deposit amount 

    Returns:
        float: total amount after specific years
    """
    try:
        total_amount = principle
        for _ in range(years):
            interest = total_amount * (annual_rate/100) # calculating interest 
            total_amount += interest                    # adding interest to total amount
            total_amount += contributions               # adding contributions to total amount
        return total_amount
    
    except Exception as e:
        return str(e)