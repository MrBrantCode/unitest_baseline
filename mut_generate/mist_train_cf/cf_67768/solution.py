"""
QUESTION:
Develop a function named `intermingle_strings` that takes three parameters: two strings `s1` and `s2`, and a special character `special_char`. The function should return a new string that intermingles characters from `s1` and `s2` in an alternating manner. If `s1` and `s2` are of different lengths, insert `special_char` in place of the missing letters from the shorter string.
"""

def intermingle_strings(s1, s2, special_char):
    # first create an empty list for hold the intermingled string
    intermingled_string = []
    
    # Getting the maximum length between two strings for the iteration
    max_length = max(len(s1), len(s2))
    
    # iterate over the range of max_length
    for i in range(max_length):
        # for each index, we first check if there is a character at that index in s1 
        if i < len(s1):
            intermingled_string.append(s1[i])
        else:
            intermingled_string.append(special_char)
            
        # then we check if there is a character at that index in s2
        if i < len(s2):
            intermingled_string.append(s2[i])
        else:
            intermingled_string.append(special_char)
            
    # finally we join all the characters in the intermingled_string list to get the final intermingled string
    return ''.join(intermingled_string)