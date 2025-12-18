"""
QUESTION:
Create a function `calculate_sgs` that takes a dictionary `sgs_params` as input, where the dictionary contains a list of property values (`prop`) and a grid. The function should calculate the mean and standard deviation of the property values and return these values as a dictionary with keys `mean` and `standard_deviation`. The function must access the `prop` and `grid` from the input dictionary, but the grid is not used in the calculation.
"""

def calculate_sgs(sgs_params):
    prop = sgs_params["prop"]
    grid = sgs_params["grid"]
    
    mean_value = sum(prop) / len(prop)
    variance = sum((x - mean_value) ** 2 for x in prop) / len(prop)
    std_deviation = variance ** 0.5
    
    return {"mean": mean_value, "standard_deviation": std_deviation}