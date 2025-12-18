"""
QUESTION:
In this kata, you've to count lowercase letters in a given string and return the letter count in a hash with 'letter' as key and count as 'value'. The key must be 'symbol' instead of string in Ruby and 'char' instead of string in Crystal.

Example: 

```python
letter_count('arithmetics') #=> {"a": 1, "c": 1, "e": 1, "h": 1, "i": 2, "m": 1, "r": 1, "s": 1, "t": 2}
```
"""

def count_lowercase_letters(s: str) -> dict:
    """
    Counts the occurrences of each lowercase letter in the given string and returns a dictionary
    with the letters as keys and their counts as values.

    :param s: A string containing lowercase letters.
    :return: A dictionary with letters as keys and their counts as values.
    """
    from collections import Counter
    return Counter(s)