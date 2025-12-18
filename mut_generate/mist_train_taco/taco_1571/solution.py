"""
QUESTION:
Create a function that accepts 3 inputs, a string, a starting location, and a length.  The function needs to simulate the string endlessly repeating in both directions and return a substring beginning at the starting location and continues for length.

Example:
```python
endless_string('xyz', -23, 6) == 'yzxyzx'
```
To visualize:

           Negative                               Positive
    3         2         1         *         1         2         3      
    0987654321098765432109876543210123456789012345678901234567890
    xyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzxyzx
           ******
         -23 for a length of 6 == 'yzxyzx'
       
Some more examples:
```python
endless_string('xyz', 0, 4) == 'xyzx'
endless_string('xyz', 19, 2) == 'yz'
endless_string('xyz', -4, -4) == 'zxyz'
```

A negative length needs to include the starting postion and return the characters to the left of the starting position.
"""

from itertools import cycle, islice

def get_endless_substring(string: str, start: int, length: int) -> str:
    """
    Returns a substring from an endlessly repeating string starting at the given location and of the specified length.

    :param string: The input string that will be treated as endlessly repeating.
    :param start: The starting location in the endlessly repeating string.
    :param length: The length of the substring to return. If negative, it indicates the number of characters to the left of the starting position.
    :return: The substring extracted from the endlessly repeating string.
    """
    # Calculate the effective starting index
    i = (start + (length + 1 if length < 0 else 0)) % len(string)
    
    # Use cycle to simulate the endlessly repeating string
    endless_cycle = cycle(string)
    
    # Use islice to get the desired substring
    substring = ''.join(islice(endless_cycle, i, i + abs(length)))
    
    return substring