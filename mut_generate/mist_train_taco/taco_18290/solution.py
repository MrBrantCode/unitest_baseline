"""
QUESTION:
The goal of this kata is to write a function that takes two inputs: a string and a character. The function will count the number of times that character appears in the string. The count is case insensitive.

For example: 

```python
count_char("fizzbuzz","z") => 4
count_char("Fancy fifth fly aloof","f") => 5
```

The character can be any alphanumeric character. 

Good luck.
"""

def count_char_occurrences(input_string: str, target_char: str) -> int:
    """
    Counts the number of times a given character appears in a string, ignoring case.

    Parameters:
    input_string (str): The string in which to count the character.
    target_char (str): The character to count in the string.

    Returns:
    int: The number of times the character appears in the string.
    """
    return input_string.lower().count(target_char.lower())