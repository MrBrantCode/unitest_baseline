"""
QUESTION:
Create a function `convert_pantone_to_cmyk` that takes a list of Pantone color codes and returns a list of their corresponding CMYK values. If a Pantone color code is invalid, the function should return a unique error message for that code instead. Assume a dictionary `pantone_to_cmyk` is already available, mapping Pantone color codes to their CMYK values.
"""

def convert_pantone_to_cmyk(pantone_codes):
    # Given a massive dictionary mapping Pantone color codes to CMYK values
    pantone_to_cmyk = {
        # 'Pantone-Code': (Cyan, Magenta, Yellow, Key),
        'Yellow C': (0, 0, 100, 0),
        'Warm Red C': (0, 85, 89, 0),
        # And so on...
    }
    cmyk_values = []
    for code in pantone_codes:
        try:
            cmyk_values.append(pantone_to_cmyk[code])
        except KeyError:
            cmyk_values.append(f"Error: {code} is not a valid Pantone color code.")
    return cmyk_values