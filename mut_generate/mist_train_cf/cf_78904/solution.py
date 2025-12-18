"""
QUESTION:
Write a function `distinctEchoSubstrings` that takes a string `text` as input and returns the number of distinct non-empty substrings of `text` that can be written as the concatenation of some string with itself and do not contain any vowels. The input string `text` has a length between 1 and 2000 and consists of only lowercase English letters.
"""

def distinctEchoSubstrings(text: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    res = set()
    if len(text) < 2:
        return 0

    start = 0
    end = 2

    while end <= len(text):
        temp = text[start:end]
        if temp[:len(temp)//2] == temp[len(temp)//2:] and not vowels.intersection(temp):
            res.add(temp)
        if end == len(text):
            start += 1
            end = start + 2
        else:
            end += 1
    return len(res)