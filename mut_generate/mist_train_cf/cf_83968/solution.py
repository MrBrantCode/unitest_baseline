"""
QUESTION:
Design a Python program that includes an independent function named `extract_substring` to extract the substring that exists between two given words within a text. The function should handle edge cases including the lack of specified words and string configurations that result in no substring existing. 

Additionally, include another independent function named `is_palindrome` to check if a string is a palindrome. The program should be able to print out the message "The extracted string is a palindrome" if the extracted string is a palindrome.
"""

def extract_substring(word1, word2, text):
    try:
        start = text.index(word1) + len(word1)
        end = text.index(word2, start)
        return text[start:end].strip()
    except ValueError:
        return ""

def is_palindrome(s):
    return s.lower() == s.lower()[::-1]