"""
QUESTION:
Write a function `re_sub_position` that takes three parameters: `string`, `pattern`, and `position`. The function should use the `re.sub` method with the `position` argument to replace occurrences of `pattern` in `string` starting from the specified `position`. Implement this function with the understanding that the time complexity of this approach may vary depending on the complexity of the pattern and its possible matches, but is generally linear with respect to the size of the input string.
"""

import re

def re_sub_position(string, pattern, position):
    """
    Replaces occurrences of pattern in string starting from the specified position.

    Args:
    string (str): The input string.
    pattern (str): The pattern to be replaced.
    position (int): The starting position in the input string.

    Returns:
    str: The modified string with the pattern replaced.
    """
    return re.sub(pattern, '', string[position:], count=0)