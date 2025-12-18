"""
QUESTION:
Create a function called `longestSubstring` that takes a string `s` as input and returns the length of the longest substring without repeating characters. The function should not use any external libraries and should only use built-in data structures. The input string `s` will contain only lowercase letters.
"""

def longestSubstring(s): 
    length = len(s) 
    longest_string = 0
    i = 0
       
    while (i < length): 
   
        last_char_index = -1
        string_set = set() 
        current_string = 0
          
        for j in range(i, length): 
  
            if s[j] in string_set: 
                last_char_index = j 
                break
  
            else: 
                string_set.add(s[j]) 
  
                current_string += 1
              
        if longest_string < current_string: 
            longest_string = current_string 
  
        i = last_char_index + 1 if last_char_index != -1 else length 
  
    return longest_string