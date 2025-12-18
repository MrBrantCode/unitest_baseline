"""
QUESTION:
Implement a function `reverse_string(s: str) -> str` that reverses the input string `s` without using built-in string or list reversal functions. The function should efficiently handle Unicode characters and special characters without compromising their original translation, and it should use O(n) additional space.
"""

def reverse_string(s: str) -> str:
  s = list(s)
  left, right = 0, len(s) - 1
  while left < right:
    s[left], s[right] = s[right], s[left]
    left, right = left + 1, right - 1
  return ''.join(s)