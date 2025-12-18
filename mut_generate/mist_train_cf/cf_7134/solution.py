"""
QUESTION:
Implement a function `reverseWords(s: str) -> str` that takes a string of lowercase English letters and spaces as input, reverses the characters in each word in-place without using additional space, and returns the resulting string with the original word order maintained. The input string will have a maximum length of 10^4, contain only single spaces between words, and no leading or trailing spaces.
"""

def reverseWords(s: str) -> str:
    words = s.split()
    
    for i in range(len(words)):
        word = list(words[i])
        start, end = 0, len(word) - 1
        
        while start < end:
            word[start], word[end] = word[end], word[start]
            start += 1
            end -= 1
        
        words[i] = ''.join(word)
    
    return ' '.join(words)