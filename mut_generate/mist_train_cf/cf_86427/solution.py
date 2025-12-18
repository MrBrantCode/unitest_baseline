"""
QUESTION:
Write a function named `reverse_words` that takes a string as an argument. The function should reverse the order of the words in the string while maintaining the original order of characters within each word. It should also remove any leading or trailing spaces from the reversed string and collapse multiple consecutive spaces between words into a single space. The function must have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1).
"""

def reverse_words(s):
    # Remove leading and trailing spaces
    s = s.strip()

    # Split the string into a list of words
    words = s.split()

    # Reverse the order of the words
    reversed_words = words[::-1]

    # Join the reversed words into a string
    reversed_string = ' '.join(reversed_words)

    return reversed_string