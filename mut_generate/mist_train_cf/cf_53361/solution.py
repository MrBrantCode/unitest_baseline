"""
QUESTION:
Design a function named `reverseAlphabets` that takes a string `s` as input. The function should reverse the alphabets in the string while keeping the positions of non-alphabetic characters (digits and special characters) unchanged. The function should preserve the capitalization of the alphabets in the reversed string.
"""

def reverseAlphabets(s):
  r = list(s)
  i, j  = 0, len(s) - 1

  while i < j:
    if not r[i].isalpha():
      i += 1
    elif not r[j].isalpha():
      j -= 1
    else:
      r[i], r[j] = r[j], r[i]
      i += 1  
      j -= 1  

  return "".join(r)