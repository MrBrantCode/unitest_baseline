"""
QUESTION:
Write a function `longPalSubstr(s)` that finds and returns the longest palindromic substring in a given string `s`. The function should iterate over the string to find all possible palindromic substrings, both odd and even in length, and keep track of the longest one found. The time complexity of the function should be O(n^2), where n is the length of the string.
"""

def longPalSubstr(s):
  def expandAround(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return r - l - 1
  if not s:
    return ""
  start= 0
  end = 0
  for i in range(len(s)):
    len1 = expandAround(s, i, i)
    len2 = expandAround(s, i, i + 1)
    size = max(len1, len2)
    if size > end - start:
        start = i - (size - 1) // 2
        end = i + size // 2
  return s[start:end + 1]