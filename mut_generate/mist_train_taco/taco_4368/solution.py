"""
QUESTION:
In this kata, you will do addition and subtraction on a given string. The return value must be also a string.

**Note:** the input will not be empty.

## Examples

```
"1plus2plus3plus4"  --> "10"
"1plus2plus3minus4" -->  "2"
```
"""

def calculate_string_expression(s: str) -> str:
    """
    Calculate the result of an arithmetic expression given as a string.
    
    The string contains numbers and the words "plus" and "minus". The result
    is returned as a string.
    
    Parameters:
    s (str): The arithmetic expression as a string.
    
    Returns:
    str: The result of the arithmetic expression as a string.
    """
    return str(sum((int(n) for n in s.replace('minus', 'plus-').split('plus'))))