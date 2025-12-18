"""
QUESTION:
Write a function to split a string and convert it into an array of words. For example:

```python
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
```
"""

def split_string_to_array(string: str) -> list:
    """
    Splits a given string into an array of words.

    Parameters:
    string (str): The input string to be split.

    Returns:
    list: A list of words obtained by splitting the input string.
    """
    return string.split(' ')