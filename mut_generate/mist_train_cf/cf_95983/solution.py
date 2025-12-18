"""
QUESTION:
Implement a function called `substring` that takes three parameters: a string and two integers `a` and `b`. The function should return a substring of the input string starting from index `a` and ending at index `b`. The implementation must not use built-in substring or slice functions. The function should handle edge cases where the input string is empty, `a` is greater than `b`, `a` or `b` is negative, or `a` or `b` exceeds the string length.
"""

def substring(string, a, b):
    if not string:  
        return ""
    if a > b or a < 0 or b < 0:  
        return ""
    if a >= len(string):  
        return ""
    if b >= len(string):  
        b = len(string) - 1
    
    substring = ""  
    
    for i in range(len(string)):  
        if i >= a and i <= b:  
            substring += string[i]  
    
    return substring  