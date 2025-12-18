"""
QUESTION:
Create a function `isAlt()` that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) and consonants are in alternate order.

```python
is_alt("amazon")
// true
is_alt("apple")
// false
is_alt("banana")
// true
```

Arguments consist of only lowercase letters.
"""

import re

def is_alt(s: str) -> bool:
    """
    Validates whether the vowels (a, e, i, o, u) and consonants in the string are in alternate order.

    Parameters:
    s (str): The input string consisting of only lowercase letters.

    Returns:
    bool: True if vowels and consonants are in alternate order, False otherwise.
    """
    return not re.search('[aeiou]{2}|[^aeiou]{2}', s)