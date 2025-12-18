"""
QUESTION:
Write a function `longestSubstring` that finds the length of the longest substring of a given string without repeating characters. The function should take a string as input and return the maximum length of the substring. The function should handle cases where the string contains repeating characters and should return the maximum length found so far.
"""

def longestSubstring(string): 
    start_index = max_length = 0
    visited = {} 
  
    # traverse through the string  
    for i in range(len(string)):  
        if string[i] in visited and start_index <= visited[string[i]]: 
            start_index = visited[string[i]] + 1
        else: 
            max_length = max(max_length, i - start_index + 1) 
  
        visited[string[i]] = i 
  
    return max_length