"""
QUESTION:
Create a function 'subStr' that takes a string 's', a start index, an end index, and an optional parameter 'step' with a default value of 1. The function should return a substring between the start and end index, and if 'step' is provided, return every nth character in that substring where n is the value of 'step'. If 'step' is negative, the function should return the substring in reverse order while still returning every nth character. The function should handle invalid inputs, including an empty string, invalid indices (start index greater than end index, start index less than 0, or end index greater than the string length), and a step of zero.
"""

def subStr(s, start, end, step=1):
    if not s:
        return "Error: The string is empty."
    if start > end or start < 0 or end > len(s):
        return "Error: Invalid indices."
    if step == 0:
        return "Error: Step cannot be zero."
    
    if step > 0:
        return s[start:end:step]
    else:
        return s[start:end:step][::-1]