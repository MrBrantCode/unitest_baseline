"""
QUESTION:
Create a function `reverse_order_of_words` that takes a string as input, manually reverses the order of its words, and returns the resulting string. The input string may contain multiple spaces between words, and the output string should have single spaces between words. The function should not use any built-in string manipulation methods or functions for reversing or splitting the string.
"""

def reverse_order_of_words(s):
    i = len(s) - 1
    end = len(s)
    result = ''
    while i >= 0:
        if s[i] == ' ':
            if end - i > 1:  
                if len(result) != 0:  
                    result += ' '
                result += s[i+1:end]
            end = i
        elif i == 0:  
            if len(result) != 0:  
                result += ' '
            result += s[i:end]
        i -= 1
    return result