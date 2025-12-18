"""
QUESTION:
Write a function `count_substring` that takes two parameters: `string` and `sub_string`. The function should return the number of times the `sub_string` appears in the `string`. The function should be case-sensitive and count overlapping occurrences.
"""

def count_substring(string, sub_string): 
    count = 0
  
    # Loop over the length of string 
    for i in range(0, len(string)): 
        # If a part of string matches with sub_string 
        # increment count  
        if (string[i:i+ len(sub_string)] ==sub_string): 
            count += 1
  
    return count