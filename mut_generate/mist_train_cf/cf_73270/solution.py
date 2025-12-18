"""
QUESTION:
Create a function `Reverse_text` that takes a string as input and returns the string in reverse order. The function should be implemented using recursion, should not use any pre-existing functions or external libraries, and should handle errors or exceptions for unexpected inputs. The algorithm should have a time complexity of O(n) or better.
"""

def Reverse_text(string, index=0):
    try:
        if not string or index > len(string) - 1:
            return ''
        return string[-(index + 1)] + Reverse_text(string, index + 1)
    except TypeError:
        return 'Unexpected input.'