"""
QUESTION:
Write a function named `minSteps` that takes three strings `s`, `t`, and `p` as input, and returns the minimum number of steps to make `t` an anagram of `s` using only characters from `p`. If it's not possible to make `t` an anagram of `s` using only characters from `p`, return -1.

Note that the input strings `s`, `t`, and `p` contain lower-case English letters only, `s.length == t.length`, and `1 <= s.length, p.length <= 50000`.
"""

from collections import Counter

def minSteps(s, t, p):
  s = Counter(s)
  t = Counter(t)
  p = Counter(p)
  
  diff = 0
  for key, value in s.items():
    if key not in t:
      if p[key] >= value:
        diff += value
      else:
        return -1
    else:
      if value > t[key]:
        if p[key] >= value-t[key]:
          diff += value-t[key]
        else:
          return -1

  return diff