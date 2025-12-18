"""
QUESTION:
Given a string ``string`` that contains only letters, you have to find out the number of **unique** strings (including ``string`` itself) that can be produced by re-arranging the letters of the ``string``.  Strings are case **insensitive**.

HINT: Generating all the unique strings and calling length on that isn't a great solution for this problem. It can be done a lot faster...

## Examples

```python
uniqcount("AB") = 2      # "AB", "BA"
uniqcount("ABC") = 6     # "ABC", "ACB", "BAC", "BCA", "CAB", "CBA"
uniqcount("ABA") = 3     # "AAB", "ABA", "BAA"
uniqcount("ABBb") = 4    # "ABBB", "BABB", "BBAB", "BBBA"
uniqcount("AbcD") = 24   # "ABCD", etc.
```
"""

from operator import mul
from functools import reduce
from collections import Counter
from math import factorial as fact

def count_unique_permutations(string: str) -> int:
    """
    Calculate the number of unique permutations of the input string, considering case insensitivity.

    Parameters:
    string (str): The input string containing only letters.

    Returns:
    int: The number of unique permutations of the input string.
    """
    # Convert the string to lowercase to handle case insensitivity
    lower_string = string.lower()
    
    # Count the frequency of each character in the string
    char_counts = Counter(lower_string)
    
    # Calculate the factorial of the length of the string
    total_permutations = fact(len(lower_string))
    
    # Divide by the factorial of the counts of each character to account for duplicates
    unique_permutations = total_permutations // reduce(mul, map(fact, char_counts.values()), 1)
    
    return unique_permutations