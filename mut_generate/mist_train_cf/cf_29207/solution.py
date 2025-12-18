"""
QUESTION:
Implement a function `convertInput(inputType, inputString)` that converts an input string into a specific data type based on the provided type. The function should handle three different types: `Color`, `Vec4`, and `Int`. 

The function takes two parameters: `inputType` (string) and `inputString` (string). The `inputType` parameter can be one of the following: "Color", "Vec4", or "Int". The `inputString` parameter represents the data to be converted. 

The conversion rules are as follows:
- For `Color` and `Vec4`, the input string should represent four float values separated by spaces. The function should return these values as a list or tuple of floats.
- For `Int`, the input string should represent a single integer value. The function should return this value as an integer.
"""

def convertInput(inputType, inputString):
    if inputType == "Color":
        return tuple(map(float, inputString.split()))
    elif inputType == "Vec4":
        return tuple(map(float, inputString.split()))
    elif inputType == "Int":
        return int(inputString)