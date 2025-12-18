"""
QUESTION:
Create a function called `reverse_and_capitalize` that takes a string as input, capitalizes all the letters, reverses the order of words, and removes all vowels. The function should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(1), without using additional data structures or variables that scale with the input size.
"""

def reverse_and_capitalize(s):
    s = s.upper()
    words = s.split()
    result = []
    for word in words:
        consonants = [c for c in word if c.lower() not in 'aeiou']
        result.append(''.join(consonants))
    return ' '.join(reversed(result))