"""
QUESTION:
Construct a function `sum_of_digits` that takes a mixed character string of alphabets and digits as an input parameter. The function should isolate every individual numeric digit from the string, calculate the sum of these separated digits, and return the calculated sum. The input string can be assumed to be non-empty and may contain any combination of alphabets and digits.
"""

def sum_of_digits(input_string):
    sum_ = 0
    for character in input_string:
        if character.isdigit():   # Check if the character is a digit
            sum_ += int(character)   # Convert the character to integer and add it to the sum
    return sum_