"""
QUESTION:
Given a string, swap the case for each of the letters.

e.g. CodEwArs --> cODeWaRS

### Examples

```
""           ->   ""
"CodeWars"   ->   "cODEwARS"
"abc"        ->   "ABC"
"ABC"        ->   "abc"
"123235"     ->   "123235"
```
"""

def swap_case(input_string: str) -> str:
    """
    Swaps the case for each letter in the input string.

    Parameters:
    input_string (str): The string for which the case of each letter needs to be swapped.

    Returns:
    str: A new string with the case of each letter swapped.
    """
    return input_string.swapcase()