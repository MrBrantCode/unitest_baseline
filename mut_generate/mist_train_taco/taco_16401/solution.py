"""
QUESTION:
In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

```python
permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
```

The order of the permutations doesn't matter.
"""

import itertools

def generate_unique_permutations(input_string: str) -> list[str]:
    """
    Generate all unique permutations of the input string.

    Parameters:
    input_string (str): The input string for which permutations are to be generated.

    Returns:
    list[str]: A list of unique permutations of the input string.
    """
    return list(set(''.join(p) for p in itertools.permutations(input_string)))