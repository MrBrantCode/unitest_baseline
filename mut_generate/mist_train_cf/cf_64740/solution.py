"""
QUESTION:
Develop a function `remove_padding_characters` that takes two arguments: a string `text` and a list of characters `chars` to be removed from the string. The function should remove all occurrences of characters in `chars` from the string, preserving the structure of words and sentences. Note that `chars` may include whitespace characters like spaces, tabs, and newlines.
"""

def remove_padding_characters(text, chars):
    words = text.split()
    cleaned_words = []
    for word in words:
        for ch in chars:
            if ch in word:
                word = word.replace(ch, '')
        cleaned_words.append(word)
    cleaned_text = ' '.join(cleaned_words)
    return cleaned_text