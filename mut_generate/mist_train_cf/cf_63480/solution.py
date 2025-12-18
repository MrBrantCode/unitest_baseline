"""
QUESTION:
Write a function `convert_phrase` that takes a phrase as input, converts the first letter of each word to uppercase, replaces all vowels (both lowercase and uppercase) in the remaining parts of the words with 'z', and returns the resulting string. The function should handle punctuation attached to words correctly.
"""

def convert_phrase(phrase):
    vowels = 'aeiou'
    return ' '.join(
        word[0].upper() + 
        ''.join('z' if char.lower() in vowels else char for char in word[1:])
        for word in phrase.split()
    )