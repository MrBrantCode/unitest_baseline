"""
QUESTION:
Take an input string and return a string that is made up of the number of occurences of each english letter in the input followed by that letter, sorted alphabetically. The output string shouldn't contain chars missing from input (chars with 0 occurence); leave them out.

An empty string, or one with no letters, should return an empty string.

Notes:

* the input will always be valid;
* treat letters as **case-insensitive**


## Examples

```
"This is a test sentence."  ==>  "1a1c4e1h2i2n4s4t"
""                          ==>  ""
"555"                       ==>  ""
```
"""

from collections import Counter

def count_letter_occurrences(input_string: str) -> str:
    # Convert the input string to lowercase and filter out non-alphabetic characters
    cnt = Counter((c for c in input_string.lower() if c.isalpha()))
    
    # Sort the letters alphabetically and format the result as "numberletter"
    result = ''.join((str(n) + c for (c, n) in sorted(cnt.items())))
    
    return result