"""
QUESTION:
Write a function `calculate_updated_area` that takes four arguments: the original length and width of a rectangle, and the percentage increase in length and width. The function should calculate the new area of the rectangle after the increase and return it. The function should also handle invalid inputs, including non-numeric values and negative or zero values for the dimensions or percentage increases, and return an error message in such cases.
"""

def calculate_updated_area(orig_length, orig_width, perc_increase_length, perc_increase_width):
    if (type(orig_length) not in [int, float]) or (type(orig_width) not in [int, float]) or (type(perc_increase_length) not in [int, float]) or (type(perc_increase_width) not in [int, float]):
        return "Error: Invalid input. Dimensions and percentage increases must be numbers."
    elif (orig_length <= 0) or (orig_width <= 0) or (perc_increase_length < 0) or (perc_increase_width < 0):
        return "Error: Dimensions and percentage increases must be positive."
    
    new_length = orig_length * (1 + perc_increase_length/100)
    new_width = orig_width * (1 + perc_increase_width/100)
    new_area = new_length * new_width
    
    return new_area