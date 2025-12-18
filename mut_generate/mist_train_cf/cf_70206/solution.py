"""
QUESTION:
Construct the function `checkPalindromeFormation(a: str, b: str) -> bool` to determine if it's feasible to construct a palindrome string by dividing two input strings `a` and `b` at the same index and concatenating the resulting segments. Both strings are of identical length, consisting of lowercase English letters, with a length between 1 and 10^5.
"""

def checkPalindromeFormation(a: str, b: str) -> bool:
    left, right = 0, len(a) - 1
    while left < right and a[left] == b[right]:
        left += 1
        right -= 1
    aBound = (left, right)
    left, right = 0, len(a) - 1
    while left < right and b[left] == a[right]:
        left += 1
        right -= 1
    bBound = (left, right)
    return a[aBound[0]:aBound[1]+1] == a[aBound[0]:aBound[1]+1][::-1] or b[bBound[0]:bBound[1]+1] == b[bBound[0]:bBound[1]+1][::-1]