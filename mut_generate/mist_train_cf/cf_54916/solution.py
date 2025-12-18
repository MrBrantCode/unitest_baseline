"""
QUESTION:
Create a function `convert` that takes three parameters: a distance value (`float`), the unit of the input distance (`str`), and the desired unit of the output distance (`str`). The function should convert the input distance from the given unit to the desired unit. The supported units are 'kilometer', 'nautical_mile', 'mile', 'meter', and 'yard'. If the input or output unit is not supported, the function should return an error message.
"""

def convert(dist: float, from_unit: str, to_unit: str) -> float:
    # Uniform conversion table with kilometer as base
    conversion_table = {
        "kilometer": 1.0,
        "nautical_mile": 0.539956803,
        "mile": 0.621371192,
        "meter": 1000.0,
        "yard": 1093.6133,
    }
    
    # Invert for going from some unit to kilometer
    inverted_conversion_table = {unit: 1 / factor for unit, factor in conversion_table.items()}

    # Try to lookup the conversion factor 
    try:
        result = dist * inverted_conversion_table[from_unit] * conversion_table[to_unit]
    except KeyError:
        print(f"Invalid unit(s). Units should be any of {', '.join(conversion_table.keys())}")
        return None

    return result