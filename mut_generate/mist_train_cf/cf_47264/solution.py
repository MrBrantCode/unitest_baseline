"""
QUESTION:
Write a function `check_string` that takes four parameters: a string `s`, a list of characters `chars`, a list of numbers `nums`, and a boolean `order`. The function should return `True` if each character in `chars` appears in `s` exactly the corresponding number of times in `nums`. If `order` is `True`, the function should respect the order of characters and their frequencies in the lists. If `order` is `False`, the function should only check the total frequency of each character, regardless of order.
"""

def check_string(s, chars, nums, order):
  if order:
    start = 0
    for c, n in zip(chars, nums):
      count = s[start:].count(c)
      if count != n:
        return False
      start += s[start:].find(c) + count
    return True
  else:
    for c, n in zip(chars, nums):
      if s.count(c) != n:
        return False
    return True