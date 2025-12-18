"""
QUESTION:
Your job is to write a function which increments a string, to create a new string.

- If the string already ends with a number, the number should be incremented by 1.
- If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

`foo -> foo1`

`foobar23 -> foobar24`

`foo0042 -> foo0043`

`foo9 -> foo10`

`foo099 -> foo100`

*Attention: If the number has leading zeros the amount of digits should be considered.*
"""

def increment_string(strng):
    # Separate the string into the head (non-numeric part) and tail (numeric part)
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    
    # If there is no numeric part, append '1' to the original string
    if tail == '':
        return strng + '1'
    
    # Increment the numeric part and ensure it has the same length with leading zeros
    return head + str(int(tail) + 1).zfill(len(tail))