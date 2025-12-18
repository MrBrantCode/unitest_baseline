"""
QUESTION:
In this exercise, a string is passed to a method and a new string has to be returned with the first character of each word in the string.

For example:

```
"This Is A Test" ==> "TIAT"
```
"""

def extract_first_characters(input_string: str) -> str:
    """
    Extracts the first character of each word in the input string and returns a new string containing these characters.

    Parameters:
    input_string (str): The input string from which to extract the first characters of each word.

    Returns:
    str: A new string containing the first character of each word from the input string.
    """
    return ''.join((word[0] for word in input_string.split()))