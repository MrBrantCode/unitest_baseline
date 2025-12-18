"""
QUESTION:
# Task
A newspaper is published in Walrusland. Its heading is `s1` , it consists of lowercase Latin letters. 

Fangy the little walrus wants to buy several such newspapers, cut out their headings, glue them one to another in order to get one big string. 

After that walrus erase several letters from this string in order to get a new word `s2`. 

It is considered that when Fangy erases some letter, there's no whitespace formed instead of the letter. That is, the string remains unbroken and it still only consists of lowercase Latin letters.

For example, the heading is `"abc"`. If we take two such headings and glue them one to the other one, we get `"abcabc"`. If we erase the 1st letter("a") and 5th letter("b"), we get a word `"bcac"`.

Given two string `s1` and `s2`, return the least number of newspaper headings `s1`, which Fangy will need to receive the word `s2`. If it is impossible to get the word `s2` in the above-described manner, return `-1`.

# Example

For `s1="abc", s2="bcac"`, the output should be `2`.

```
"abcabc" --> "bcac"
 x   x
```

For `s1="abc", s2="xyz"`, the output should be `-1`.

It's impossible to get the word `s2`.
"""

import re

def minimum_newspapers_needed(s1: str, s2: str) -> int:
    # Create a pattern by replacing each character in s1 with itself followed by a '?'
    pattern = re.sub('(.)', '\\1?', s1)
    
    # Check if all characters in s2 are present in s1
    if set(s2) - set(s1):
        return -1
    
    # Find all matches of the pattern in s2
    matches = re.findall(pattern, s2)
    
    # The number of matches minus one gives the minimum number of s1 needed
    return len(matches) - 1