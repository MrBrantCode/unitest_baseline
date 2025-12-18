"""
QUESTION:
Write a function `max_common_substring_length(s, t, u)` that determines the maximal length of the identical substring sequence shared by three text strings `s`, `t`, and `u`, with the restriction that the shared substring must not contain vowels. 

The function should return the length of the longest common substring without vowels.
"""

def max_common_substring_length(s, t, u):
  max_length = 0
  min_length_string = min(s, t, u, key=len)
  vowels = set('aeiouAEIOU')
  
  for i in range(len(min_length_string)):
    for j in range(i+1, len(min_length_string)+1):
      substring = min_length_string[i:j]
      
      if not any(char in vowels for char in substring):
        if substring in s and substring in t and substring in u:
          max_length = max(max_length, len(substring))
          
  return max_length