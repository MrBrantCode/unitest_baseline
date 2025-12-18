"""
QUESTION:
Given a string, return a new string that has transformed based on the input:

* Change case of every character, ie. lower case to upper case, upper case to lower case.
* Reverse the order of words from the input.

**Note:** You will have to handle multiple spaces, and leading/trailing spaces.

For example:

```
"Example Input" ==> "iNPUT eXAMPLE"
```

You may assume the input only contain English alphabet and spaces.
"""

def transform_string(s: str) -> str:
    """
    Transforms the input string by changing the case of every character and reversing the order of words.

    Parameters:
    s (str): The input string containing only English alphabet and spaces.

    Returns:
    str: A new string with the case of every character changed and the order of words reversed.
    """
    return ' '.join(s.swapcase().split(' ')[::-1])