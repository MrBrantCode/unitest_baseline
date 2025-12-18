"""
QUESTION:
Write a recursive function `count_lower_alphabets` that takes a string as input and returns the number of lowercase alphabets in the string, excluding 'a' and 'b'. The function should handle cases where the input string contains special characters, digits, or whitespace, and only count lowercase alphabets within the range of 'c' to 'z'.
"""

def count_lower_alphabets(string):
    # Base case: if string is empty, return 0
    if len(string) == 0:
        return 0

    # Recursive case: check the first character of the string
    if string[0].islower() and string[0] >= 'c' and string[0] <= 'z':
        # If the first character is a lowercase alphabet within the range of 'c' to 'z',
        # increment the count by 1 and make a recursive call with the remaining characters
        return 1 + count_lower_alphabets(string[1:])
    else:
        # If the first character is not a lowercase alphabet within the range of 'c' to 'z',
        # make a recursive call with the remaining characters
        return count_lower_alphabets(string[1:])