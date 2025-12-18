"""
QUESTION:
Write a function called `find_substring` that takes a list of strings as input and returns the lengthiest sequential, alphabetic substring that is uniformly present in every single array element. The function should return an empty string if no such substring exists or if the input list is empty.
"""

def find_substring(lst):
  if not lst:
    return ""
  
  first = min(lst, key=len)
  for l in range(len(first), 0, -1):
    for s in range(len(first)-l+1):
      found = all(first[s:s+l] in other for other in lst)
      if found:
        return first[s:s+l]
      
  return ""