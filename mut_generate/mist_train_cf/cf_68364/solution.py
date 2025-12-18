"""
QUESTION:
Write a function `swap_characters(string)` that takes a string as input and returns a new string where the characters at even and odd index positions are swapped. Assume 0-based indexing, where the first character is at an even index and the second character is at an odd index. If the string has an odd length, the last character should remain in its original position.
"""

def swap_characters(string):
    # convert string into list to allow assignment
    str_list = list(string)     
   
    # loop for every two elements in the list, and swap them
    for i in range(0, len(str_list)-1, 2): 
        str_list[i], str_list[i+1] = str_list[i+1], str_list[i]
   
    # return combined list as string 
    return ''.join(str_list)