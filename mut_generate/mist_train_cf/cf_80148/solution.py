"""
QUESTION:
Write a function called `reverse_phrases` that takes a string of English greeting phrases separated by commas as input. The function should reverse the order of words in each phrase without reversing the order of the phrases themselves. The commas should remain in their original positions. The input string may contain phrases with multiple words and punctuation marks.
"""

def reverse_phrases(text):
    phrases = text.split(',')
    reversed_phrases = [' '.join(phrase.split()[::-1]) for phrase in phrases]
    return ','.join(reversed_phrases)