"""
QUESTION:
Implement the `get_reverseOnlyLetters` function which takes a string `S` as input and returns a string with only the alphabetical characters reversed. Non-alphabetical characters should remain in their original positions. The reversed alphabetical characters should be replaced in the order they appear in the original string.
"""

def reverseOnlyLetters(S):
    S = list(S)
    letters = [c for c in S if c.isalpha()]
    letters.reverse()
    j = 0

    for i in range(len(S)):
        if S[i].isalpha():
            S[i] = letters[j]
            j += 1

    return "".join(S)