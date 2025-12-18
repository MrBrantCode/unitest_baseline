"""
QUESTION:
Write a function called `reverse_ascii_sum` that takes a string as input, reverses it, calculates the ASCII value of each character in the reversed string, and returns the sum of these ASCII values. The function should handle any exceptions that occur during execution.
"""

def reverse_ascii_sum(s):
    try:
        reversed_str = s[::-1]
        return sum(ord(char) for char in reversed_str)
    except Exception as error:
        print(f"An error occured: {error}")