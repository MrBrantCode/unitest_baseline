"""
QUESTION:
Write a function called `LCS` that accepts two sequences and returns the longest subsequence common to the passed in sequences.

### Subsequence
A subsequence is different from a substring. The terms of a subsequence need not be consecutive terms of the original sequence.

### Example subsequence
Subsequences of `"abc"` = `"a"`, `"b"`, `"c"`, `"ab"`, `"ac"`, `"bc"` and `"abc"`.

### LCS examples
```python
lcs( "abcdef" , "abc" ) => returns "abc"
lcs( "abcdef" , "acf" ) => returns "acf"
lcs( "132535365" , "123456789" ) => returns "12356"
```

### Notes
* Both arguments will be strings
* Return value must be a string
* Return an empty string if there exists no common subsequence
* Both arguments will have one or more characters (in JavaScript)
* All tests will only have a single longest common subsequence. Don't worry about cases such as `LCS( "1234", "3412" )`, which would have two possible longest common subsequences: `"12"` and `"34"`.

Note that the Haskell variant will use randomized testing, but any longest common subsequence will be valid.

Note that the OCaml variant is using generic lists instead of strings, and will also have randomized tests (any longest common subsequence will be valid).

### Tips

Wikipedia has an explanation of the two properties that can be used to solve the problem:

- [First property](http://en.wikipedia.org/wiki/Longest_common_subsequence_problem#First_property)
- [Second property](http://en.wikipedia.org/wiki/Longest_common_subsequence_problem#Second_property)
"""

def longest_common_subsequence(seq1: str, seq2: str) -> str:
    """
    Finds the longest common subsequence (LCS) of two given sequences.

    Parameters:
    seq1 (str): The first sequence.
    seq2 (str): The second sequence.

    Returns:
    str: The longest common subsequence of seq1 and seq2.
    """
    if len(seq1) == 0 or len(seq2) == 0:
        return ''
    if seq1[-1] == seq2[-1]:
        return longest_common_subsequence(seq1[:-1], seq2[:-1]) + seq1[-1]
    else:
        lcs1 = longest_common_subsequence(seq1, seq2[:-1])
        lcs2 = longest_common_subsequence(seq1[:-1], seq2)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2