"""
QUESTION:
Write a function `remove_whitespaces(string)` that takes a string as input and returns the string with all whitespaces removed, while maintaining the original order of characters. The solution should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string, and should not use any built-in string manipulation functions or regular expressions.
"""

def remove_whitespaces(string):
    string = list(string)  
    slow = 0  
    fast = 0  
    
    while fast < len(string):
        if string[fast] != ' ':
            string[slow] = string[fast]  
            slow += 1
        fast += 1
    
    return ''.join(string[:slow])  