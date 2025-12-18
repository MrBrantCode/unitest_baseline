"""
QUESTION:
Write a function `reverse_string(string)` that takes a string as input and returns a string where the order of words is reversed and each word is also reversed, without using any built-in string reversal functions or methods. The input string may contain spaces and punctuation, but does not have leading or trailing spaces.
"""

def reverse_string(string):
    words = string.split()
    reversed_words = []
    
    for word in words:
        start = 0
        end = len(word) - 1
        word_list = list(word)
        
        while start < end:
            word_list[start], word_list[end] = word_list[end], word_list[start]
            start += 1
            end -= 1
        
        reversed_words.append(''.join(word_list))
    
    reversed_string = ' '.join(reversed(reversed_words))
    return reversed_string