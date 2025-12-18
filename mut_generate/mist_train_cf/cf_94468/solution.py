"""
QUESTION:
Create a function called `convert_scientific_notation` that takes an input string containing numbers in scientific notation and/or decimal numbers separated by commas. The function should convert these numbers to integers, truncating any decimal portions, and return the results as a string with the converted integers separated by commas.
"""

def convert_scientific_notation(inputString):
    # Split the input string by commas
    numbers = inputString.split(", ")
    
    # Iterate over each number
    converted_numbers = []
    for number in numbers:
        # Convert the number from scientific notation to a float
        float_number = float(number)
        
        # Convert the float to an integer
        integer_number = int(float_number)
        
        # Append the integer to the converted_numbers list
        converted_numbers.append(integer_number)
    
    # Return the converted numbers as a string
    return ", ".join(str(number) for number in converted_numbers)