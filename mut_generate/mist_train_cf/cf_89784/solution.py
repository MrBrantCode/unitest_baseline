"""
QUESTION:
Write a function `reverseWords(s: str) -> str` that takes a string `s` as input and returns a new string where the characters in each word are reversed, while maintaining their original order in the string. The input string `s` contains only lowercase English letters and spaces, with a length of at most 10^4, and words are separated by a single space with no leading or trailing spaces. The function should reverse the words in-place, without using any additional space.
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