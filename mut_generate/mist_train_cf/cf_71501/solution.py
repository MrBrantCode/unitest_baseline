"""
QUESTION:
Write a function `palindrome_permutation(s, k)` that takes a string `s` and an integer `k` as input and returns `True` if a permutation of the string could form a palindrome and the frequency of each character in the string is less than or equal to `k`, and `False` otherwise. The string `s` consists of only lowercase English letters and has a length between 1 and 5000, and `k` is an integer between 1 and 5000.
"""

def palindrome_permutation(s, k):
  frequency_table = {}
  for letter in s: 
    if letter in frequency_table:
        frequency_table[letter] += 1
    else:
        frequency_table[letter] = 1

  odd_count = 0
  for count in frequency_table.values():
    if count % 2 != 0:
      odd_count += 1
    if count > k or odd_count > 1:
      return False

  return True