"""
QUESTION:
Implement a function `strStr` that returns the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`. The function cannot use any built-in string search functions and must implement the search algorithm itself. 

If `needle` is an empty string, the function should return 0. The function should work with strings consisting of only lower-case English characters, with lengths up to 5 * 10^5. The time complexity of the solution should be efficient to handle long strings.
"""

def strStr(haystack: str, needle: str) -> int:
    m, n = len(haystack), len(needle)
    if n == 0:
        return 0
    if m < n:
        return -1

    base = 26
    mod = 10**9 + 7

    haystack_hash = needle_hash = 0
    base_l = 1

    for i in range(n):
        haystack_hash = (haystack_hash*base + ord(haystack[i]))%mod
        needle_hash = (needle_hash*base + ord(needle[i]))%mod
        if i != n-1:
            base_l = base_l*base%mod

    if haystack_hash == needle_hash:
        return 0

    for i in range(n, m):
        haystack_hash = ((haystack_hash - ord(haystack[i-n])*base_l%mod)*base + ord(haystack[i]))%mod
        if haystack_hash == needle_hash:
            return i-n+1

    return -1