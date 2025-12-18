"""
QUESTION:
Implement a function `remove_whitespace` that takes a string as input and returns a new string with all whitespace characters removed while maintaining the original order of characters. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string, and should not use any built-in string manipulation functions or regular expressions.
"""

def remove_whitespace(s):
    s_list = list(s)
    length = len(s_list)
    count = 0
    
    for i in range(length):
        if s_list[i] != ' ':
            s_list[count] = s_list[i]
            count += 1
    
    return "".join(s_list[:count])