"""
QUESTION:
Reverse the words in a sentence while maintaining their original order and preserving punctuation marks. Write a function named `reverse_words` to achieve this.
"""

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = [word.strip('.,!?;:').lower()[::-1] + ''.join([c for c in word if not c.isalnum()]) for word in words]
    return ' '.join(reversed_words)