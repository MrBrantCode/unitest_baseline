"""
QUESTION:
Complete the function that accepts a string parameter, and reverses each word in the string. **All** spaces in the string should be retained.

## Examples
```
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
```
"""

def reverse_each_word(input_string: str) -> str:
    """
    Reverses each word in the input string while retaining all spaces.

    Parameters:
    input_string (str): The input string containing words to be reversed.

    Returns:
    str: The modified string with each word reversed, retaining all spaces.
    """
    return ' '.join((s[::-1] for s in input_string.split(' ')))