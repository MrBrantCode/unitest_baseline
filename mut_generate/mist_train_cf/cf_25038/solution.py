"""
QUESTION:
Create a function named `reverse_and_trim` that takes a string `s` as input. The function should remove all leading and trailing white spaces from the input string, then remove all spaces within the string, and finally return the resulting string in reverse order.
"""

def reverse_and_trim(s):
    s = s.strip()
    s = s.replace(" ", "")
    return s[::-1]