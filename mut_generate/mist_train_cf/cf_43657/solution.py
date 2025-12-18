"""
QUESTION:
Implement a function `transmute(number, initial_radix, secondary_radix)` that converts a given number from an initial numerical system (`initial_radix`) to a secondary radix (`secondary_radix`). Both `initial_radix` and `secondary_radix` should be between 2 and 36. The function should handle errors and return an error message if the conversion is not possible.
"""

def transmute(number, initial_radix, secondary_radix):
    """
    Converts a given number from an initial numerical system (initial_radix) to a secondary radix (secondary_radix).
    
    Args:
        number (str): The number to be converted.
        initial_radix (int): The initial numerical system.
        secondary_radix (int): The target numerical system.
    
    Returns:
        str: The converted number in the secondary radix or an error message if the conversion is not possible.
    """

    if not 2 <= initial_radix <= 36 or not 2 <= secondary_radix <= 36:
        return f"Both number systems should have a base between 2 and 36."
    try:
        dec_number = int(str(number), initial_radix)
        if secondary_radix == 10:
            return str(dec_number)
        elif secondary_radix == 2:
            return bin(dec_number)[2:]
        elif secondary_radix == 8:
            return oct(dec_number)[2:]
        elif secondary_radix == 16:
            return hex(dec_number)[2:]
        else:
            return convert_from_decimal(dec_number, secondary_radix)
    except ValueError:
        return f"Cannot convert {number} from base {initial_radix} to base {secondary_radix}."

def convert_from_decimal(number, base):
    conversion = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if number < base:
        return conversion[number]
    else:
        return convert_from_decimal(number // base, base) + conversion[number % base]