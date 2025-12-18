"""
QUESTION:
Implement a function `number_to_binary(x: str, base: int) -> str` that converts a number from a specified base (8, 10, or 16) into its binary equivalent, represented as strings. The function should optimize for time complexity and integrate error handling to ensure robustness. The function should return "Error: " followed by the corresponding error message for invalid inputs.
"""

def number_to_binary(x: str, base: int) -> str:
    try:
        # Check if the base is valid
        if base not in [8, 10, 16]:
            return "Error: Base must be 8 (octal), 10 (decimal), or 16 (hexadecimal)."

        # Check if the number is valid for the given base
        try:
            number = int(x, base)
        except ValueError:
            return "Error: The number is not valid for the given base."

        # Convert the number to binary
        return bin(number)[2:]
    except Exception as e:
        return "Error: " + str(e)