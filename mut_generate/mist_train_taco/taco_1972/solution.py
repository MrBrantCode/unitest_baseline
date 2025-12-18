"""
QUESTION:
Given an array of numbers (in string format), you must return a string. The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc. You should also account for `'!'`, `'?'` and `' '` that are represented by '27', '28' and '29' respectively.

All inputs will be valid.
"""

def decode_message(arr):
    # Create a dictionary mapping numbers to their corresponding characters
    d = {str(i): chr(123 - i) for i in range(1, 27)}
    d.update({'27': '!', '28': '?', '29': ' ', '0': ''})
    
    # Decode the message using the dictionary
    return ''.join([d[str(i)] for i in arr])