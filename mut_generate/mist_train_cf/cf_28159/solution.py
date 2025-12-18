"""
QUESTION:
Implement the `nearestPalindromic` function which takes a string `n` representing a positive integer and returns the nearest palindromic number to the given input `n`. If there are multiple nearest palindromic numbers, return the smallest one. If the input number itself is a palindrome, return the nearest palindrome that is greater than the input number. A palindrome is a number that remains the same when its digits are reversed.
"""

def nearestPalindromic(n: str) -> str:
    num = int(n)
    if num < 10:
        return str(num - 1) if num > 0 else '0'

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def get_palindrome_diff(p1: int, p2: int, num: int) -> int:
        return abs(p1 - num) - abs(p2 - num) if abs(p1 - num) != abs(p2 - num) else p1 - p2

    length = len(n)
    candidates = set()
    candidates.add(10 ** length + 1)
    candidates.add(10 ** (length - 1) - 1)

    prefix = int(n[:(length + 1) // 2])
    for i in map(str, (prefix - 1, prefix, prefix + 1)):
        if length % 2:
            candidates.add(int(i + i[:-1][::-1]))
        else:
            candidates.add(int(i + i[::-1]))

    candidates.discard(num)
    candidates = sorted(candidates)

    min_diff = float('inf')
    res = ''
    for candidate in candidates:
        diff = abs(candidate - num)
        if diff < min_diff:
            min_diff = diff
            res = str(candidate)
        elif diff == min_diff:
            res = min(res, str(candidate), key=lambda x: (abs(int(x) - num), int(x)))
    return res