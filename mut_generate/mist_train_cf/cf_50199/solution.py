"""
QUESTION:
Write a function named `cups_to_gallons` that calculates the volume of soup needed in gallons when given the number of cups brewed last year. The function should double the number of cups and then convert the total to gallons, knowing that 1 gallon is equivalent to 16 cups.
"""

def cups_to_gallons(cups_last_year):
    """
    Calculate the volume of soup needed in gallons when given the number of cups brewed last year.
    
    The function doubles the number of cups and then converts the total to gallons.
    
    Parameters:
    cups_last_year (int): The number of cups brewed last year.
    
    Returns:
    float: The volume of soup needed in gallons.
    """
    cups_per_gallon = 16
    cups_this_year = cups_last_year * 2
    gallons_this_year = cups_this_year / cups_per_gallon
    return gallons_this_year