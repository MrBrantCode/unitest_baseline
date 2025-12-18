"""
QUESTION:
Write a function that returns the count of characters that have to be removed in order to get a string with no consecutive repeats.

*Note:* This includes any characters

##  Examples

```python
'abbbbc'  => 'abc'    #  answer: 3
'abbcca'  => 'abca'   #  answer: 2
'ab cca'  => 'ab ca'  #  answer: 1
```
"""

from itertools import groupby

def count_consecutive_repeats_to_remove(s: str) -> int:
    """
    Counts the number of characters that need to be removed from the string `s`
    to eliminate consecutive repeating characters.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of characters to remove.
    """
    return len(s) - len(list(groupby(s)))