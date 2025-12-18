"""
QUESTION:
Write a function `camel_to_snake_case` that takes a string in camelCase notation as input and returns its equivalent in snake_case notation. The function should handle both UpperCamelCase and lowerCamelCase, and preserve the position of digits and special symbols in the string. Digits should only be preceded by an underscore if they are not immediately following another digit.
"""

def camel_to_snake_case(input_str):
    # Include '_' before each uppercase character and convert it to lowercase
    output_str = ''.join('_' + i.lower() if i.isupper() else i for i in input_str)
    
    # Include '_' before each digit if it's not right after another digit
    output_str = ''.join('_' + i if i.isdigit() and not output_str[j-1].isdigit() and output_str[j-1] != '_' else i for j, i in enumerate(output_str))

    # Remove leading '_' if exists
    if output_str.startswith('_'):
        output_str = output_str[1:]
        
    return output_str