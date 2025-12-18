"""
QUESTION:
You will be given two strings `a` and `b` consisting of lower case letters, but `a` will have at most one asterix character. The asterix (if any) can be replaced with an arbitrary sequence (possibly empty) of lowercase letters. No other character of string `a` can be replaced. If it is possible to replace the asterix in `a` to obtain string `b`, then string `b` matches the pattern. 

If the string matches, return `true` else `false`. 

```
For example:
solve("code*s","codewars") = true, because we can replace the asterix(*) with "war" to match the second string. 
solve("codewar*s","codewars") = true, because we can replace the asterix(*) with "" to match the second string. 
solve("codewars","codewars") = true, because the strings already match.
solve("a","b") = false
```
More examples in test cases. 

Good luck!
"""

def matches_pattern(pattern: str, string: str) -> bool:
    """
    Determines if the given string matches the pattern where the pattern may contain at most one asterisk (*).
    The asterisk can be replaced with any sequence of lowercase letters (including an empty sequence).

    Parameters:
    - pattern (str): The pattern string that may contain at most one asterisk.
    - string (str): The string to check against the pattern.

    Returns:
    - bool: True if the string matches the pattern, False otherwise.
    """
    from fnmatch import fnmatch
    return fnmatch(string, pattern)