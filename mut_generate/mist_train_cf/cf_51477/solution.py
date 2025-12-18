"""
QUESTION:
Given a sentence `s` and an integer `k`, truncate `s` to its first `k` words and reverse their order. `s` consists of only lowercase and uppercase English letters and spaces, with no leading or trailing spaces, and each word is separated by a single space. Return the modified sentence as a string. The length of `s` is between 1 and 500, and `k` is between 1 and the number of words in `s`. 

Create a function `truncateSentence(s, k)` that implements this operation.
"""

def truncateSentence(s, k):
    words = s.split()[:k]
    return ' '.join(words[::-1])