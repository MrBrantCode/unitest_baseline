"""
QUESTION:
Implement a function `reverseWords` that takes a string `text` as input and returns a modified version of the string. The input string may contain multiple words separated by a single space and may have leading or trailing spaces. The function should reverse the order of words in the string while maintaining the order of characters within each word, and the output should not contain leading or trailing spaces. The function signature is `def reverseWords(text: str) -> str:`.
"""

def reverseWords(text: str) -> str:
    words = text.split()  
    reversed_words = ' '.join(reversed(words))  
    return reversed_words