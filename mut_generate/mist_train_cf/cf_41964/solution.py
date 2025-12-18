"""
QUESTION:
Write a function `uniqueLetterString(S: str) -> int` that calculates the sum of the uniqueness of all letters in the string `S`, where the uniqueness of a letter at a specific index `i` is defined as the number of occurrences of the letter at index `i` multiplied by the distance between the two closest occurrences of the letter to the left and right of index `i`. The string `S` consists of uppercase letters only, has a length between 1 and 10^4, and the result should be returned modulo 10^9 + 7.
"""

def uniqueLetterString(S: str) -> int:
    import string
    idxes = {ch : (-1, -1) for ch in string.ascii_uppercase}
    ans = 0
    for idx, ch in enumerate(S):
        i, j = idxes[ch]
        ans += (j - i) * (idx - j)
        idxes[ch] = j, idx
    for i, j in idxes.values():
        ans += (j - i) * (len(S) - j)
    return ans % (int(1e9) + 7)