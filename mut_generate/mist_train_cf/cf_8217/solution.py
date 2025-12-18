"""
QUESTION:
Write a function `check_number` that takes an integer as input and returns "Yes" if the number is positive, "No" if the number is negative, and "Zero" if the number is equal to zero. The function should also check if the number is within the range of -100 to 100. If the number is outside this range, return "Out of range". The function should be able to handle non-numeric inputs.
"""

def check_number(num):
    """
    This function checks if a given number is positive, negative, or zero, 
    and returns the corresponding string. It also checks if the number is 
    within the range of -100 to 100. If the number is outside this range, 
    it returns "Out of range". The function handles non-numeric inputs.
    
    Parameters:
    num (int): The input number to be checked.
    
    Returns:
    str: "Yes" if the number is positive, "No" if the number is negative, 
         "Zero" if the number is zero, and "Out of range" if the number is 
         outside the range of -100 to 100.
    """
    
    if not isinstance(num, int):
        return "Invalid input. Please enter a number."
    
    if num < -100 or num > 100:
        return "Out of range"
    elif num > 0:
        return "Yes"
    elif num < 0:
        return "No"
    else:
        return "Zero"