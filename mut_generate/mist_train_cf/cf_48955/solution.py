"""
QUESTION:
Create a function called `reverseName` that takes a string as an input, reverses the order of characters in each word while maintaining their original position in the string, and returns the result. For example, "John Doe" should become "nhoJ eoD".
"""

def reverseName(name):
    words = name.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)