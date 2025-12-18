"""
QUESTION:
Generate a dynamic HTML pie chart representing the proportion of each digit in a numerical string. The chart should display the digit value and its percentage when hovered over. The function `get_pie_data` should take a numerical string as input and return a list of dictionaries containing the value and percentage of each digit. Implement this in a way that allows for dynamic updates, cross-browser compatibility, and responsive design.
"""

def get_pie_data(numerical_string):
    """
    Generate a list of dictionaries containing the value and percentage of each digit in a numerical string.

    Args:
    numerical_string (str): A string of numerical characters.

    Returns:
    list: A list of dictionaries, where each dictionary contains the value and percentage of a digit in the input string.
    """
    total_sum = sum(int(digit) for digit in numerical_string)
    
    pie_data = [{"value": int(digit), "percentage": round((int(digit) / total_sum) * 100, 2)} for digit in numerical_string]
    return pie_data