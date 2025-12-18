"""
QUESTION:
Write a function `convert_variables(variables)` that takes a list of string variables in different formats (decimal, integer, scientific notation) and returns a list of variables in the same format as the first variable in the input list.

The input formats can be:
- Decimal: "12.34"
- Integer: "5678"
- Scientific notation: "1.234e5"

The output format is determined by the first variable in the list:
- If the first variable is in decimal format, all other variables should be converted into decimal format.
- If the first variable is in integer format, all other variables should be converted into integer format.
- If the first variable is in scientific notation format, all other variables should be converted into scientific notation format.

The output list should maintain the same order as the input list.
"""

def convert_variables(variables):
    first_variable = variables[0]
    first_format = determine_format(first_variable)
    
    converted_variables = []
    
    for variable in variables:
        if first_format == "decimal":
            converted_variables.append(convert_to_decimal(variable))
        elif first_format == "integer":
            converted_variables.append(convert_to_integer(variable))
        elif first_format == "scientific":
            converted_variables.append(convert_to_scientific(variable))
            
    return converted_variables
    
def determine_format(variable):
    if "." in variable:
        return "decimal"
    elif "e" in variable.lower():
        return "scientific"
    else:
        return "integer"
    
def convert_to_decimal(variable):
    return str(float(variable))
    
def convert_to_integer(variable):
    return str(int(float(variable)))
    
def convert_to_scientific(variable):
    return "{:.2e}".format(float(variable))