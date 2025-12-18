"""
QUESTION:
Given 2 strings, `a` and `b`, return a string of the form: `shorter+reverse(longer)+shorter.`


In other words, the shortest string has to be put as prefix and as suffix of the reverse of the longest.

Strings `a` and `b` may be empty, but not null (In C# strings may also be null. Treat them as if they are empty.).  
If `a` and `b` have the same length treat `a` as the longer producing `b+reverse(a)+b`
"""

def shorter_reverse_longer(a: str, b: str) -> str:
    # Treat null strings as empty strings
    if a is None:
        a = ""
    if b is None:
        b = ""
    
    # Determine which string is shorter and which is longer
    if len(a) < len(b):
        shorter, longer = a, b
    else:
        shorter, longer = b, a
    
    # Return the result in the required format
    return shorter + longer[::-1] + shorter