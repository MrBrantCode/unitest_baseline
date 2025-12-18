"""
QUESTION:
In this Kata, you will be given two strings `a` and `b` and your task will be to return the characters that are not common in the two strings. 

For example:
```Haskell
solve("xyab","xzca") = "ybzc" 
--The first string has 'yb' which is not in the second string. 
--The second string has 'zc' which is not in the first string. 
```
Notice also that you return the characters from the first string concatenated with those from the second string.

More examples in the tests cases. 

Good luck!

Please also try [Simple remove duplicates](https://www.codewars.com/kata/5ba38ba180824a86850000f7)
"""

def find_uncommon_characters(a: str, b: str) -> str:
    # Find the common characters between the two strings
    common_chars = set(a) & set(b)
    
    # Filter out the common characters from both strings and concatenate the results
    result = ''.join((c for c in a + b if c not in common_chars))
    
    return result