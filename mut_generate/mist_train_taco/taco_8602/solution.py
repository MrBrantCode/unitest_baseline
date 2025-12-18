"""
QUESTION:
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

```python
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
```
```C
is_isogram("Dermatoglyphics" ) == true;
is_isogram("aba" ) == false;
is_isogram("moOse" ) == false; // -- ignore letter case
```
"""

def is_isogram(string: str) -> bool:
    """
    Determines whether a given string is an isogram.

    An isogram is a word that has no repeating letters, consecutive or non-consecutive.
    The function ignores letter case.

    Parameters:
    string (str): The string to check.

    Returns:
    bool: True if the string is an isogram, False otherwise.
    """
    return len(string) == len(set(string.lower()))