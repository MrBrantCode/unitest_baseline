"""
QUESTION:
# Description:

 Find the longest successive exclamation marks and question marks combination in the string. A successive exclamation marks and question marks combination must contains two part: a substring of "!" and a substring "?", they are adjacent. 
 
 If more than one result are found, return the one which at left side; If no such a combination found, return `""`.

# Examples

```
find("!!") === ""
find("!??") === "!??"
find("!?!!") === "?!!"
find("!!???!????") === "!!???"
find("!!???!?????") === "!?????"
find("!????!!!?") === "????!!!" 
find("!?!!??!!!?") === "??!!!"
```

# Note
Please don't post issue about difficulty or duplicate. Because:
>[That's unfair on the kata creator. This is a valid kata and introduces new people to javascript some regex or loops, depending on how they tackle this problem.  --matt c](https://www.codewars.com/kata/remove-exclamation-marks/discuss#57fabb625c9910c73000024e)
"""

import re

def find_longest_exclamation_question_combination(stg: str) -> str:
    """
    Find the longest successive exclamation marks and question marks combination in the string.
    A successive exclamation marks and question marks combination must contain two parts:
    a substring of "!" and a substring "?", they are adjacent.

    If more than one result are found, return the one which is at the left side.
    If no such combination is found, return an empty string.

    :param stg: The input string to search in.
    :return: The longest successive exclamation marks and question marks combination.
    """
    matches = re.findall('(!+|\\?+)', stg)
    return max((f'{a}{b}' for (a, b) in zip(matches, matches[1:])), key=len, default='')