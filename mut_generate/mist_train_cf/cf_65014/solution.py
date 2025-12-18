"""
QUESTION:
Design a function named `convert_heat_units` that takes three parameters: a numerical value and two strings representing the unit of the value and the unit to convert to. The function should convert the given value between British Thermal Units (BTUs), Joules, Calories, and Watt-hours, handling invalid or out-of-bounds input values. The function should return the converted value or an error message if the input is invalid. The input value should be greater than zero, and both the from_unit and to_unit should be one of 'btu', 'joules', 'calories', or 'watthr'.
"""

def convert_heat_units(value, from_unit, to_unit):
    # conversion factors
    btu_to_joules = 1055.06
    btu_to_calories = 251.995
    btu_to_watthr = 0.293071
    
    joule_to_btu = 0.000947817
    joule_to_calories = 0.238846
    joule_to_watthr = 0.000277778 
    
    calories_to_btu = 0.00396832
    calories_to_joules = 4.184
    calories_to_watthr = 0.00116222
    
    watthr_to_btu = 3.41214
    watthr_to_joules = 3600
    watthr_to_calories = 860.421
   
    # error handling for out-of-bound input
    if value <= 0:
        return "Error: input value should be greater than zero"
    
    # Dictionary to map the conversion factors
    conv_factors = {
        'btu': {'joules': btu_to_joules, 'calories': btu_to_calories, 'watthr': btu_to_watthr},
        'joules': {'btu': joule_to_btu, 'calories': joule_to_calories, 'watthr': joule_to_watthr},
        'calories': {'btu': calories_to_btu, 'joules': calories_to_joules, 'watthr': calories_to_watthr},
        'watthr': {'btu': watthr_to_btu, 'joules': watthr_to_joules, 'calories': watthr_to_calories},
    }

    # check if the input units are valid
    if from_unit not in conv_factors:
        return "Error: Invalid from_unit"
    if to_unit not in conv_factors[from_unit]:
        return "Error: Invalid to_unit"

    # perform the conversion
    result = value * conv_factors[from_unit][to_unit]

    return result