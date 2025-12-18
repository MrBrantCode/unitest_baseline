"""
QUESTION:
You are given a large number as a string, with a maximum of 10^9 digits. Format the number by dividing it into groups of three digits starting from the leftmost digit, and separate each group with a comma. If the number of digits is not divisible by three, the rightmost group should have fewer than three digits. Write a function `format_number` that takes the large number as a string and returns the formatted number as a string.
"""

def entance(number):
    # Initialize an empty string to store the formatted number
    formatted_number = ""

    # Iterate through the number from left to right
    for i in range(len(number)):
        # Add the digit to the formatted number string
        formatted_number += number[i]

        # Add a comma separator after every three digits
        if (len(number) - i - 1) % 3 == 0 and i != len(number) - 1:
            formatted_number += ","

    # Return the formatted number
    return formatted_number