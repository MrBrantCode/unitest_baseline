"""
QUESTION:
Replace all words that start with a vowel (A, E, I, O, U) and have 5 letters or more, excluding the word "example", with "*****" in a given text.
"""

def entrance(text):
    vowels = 'aeiouAEIOU'
    words = text.split()
    new_words = []

    for word in words:
        if word[0] in vowels and len(word) >= 5 and word.lower() != 'example':
            new_words.append('*****')
        else:
            new_words.append(word)

    return ' '.join(new_words)