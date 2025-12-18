"""
QUESTION:
Create a function called `reverse_order_ignore_punctuation` that takes a string `s` as input and returns a new string where the order of words is reversed and punctuation is kept at the end of the word it was attached to. The function should not use predefined functions for reversing words, such as `split` and `join`.
"""

def reverse_order_ignore_punctuation(s):
    import string

    words = []
    word = ''
    punctuation = ''
    for ch in s:
        if ch not in string.punctuation + ' ':
            if punctuation:
                 word += punctuation
                 punctuation = ''
            word += ch
        else:
            if word:
                words.append(word)
                word = ''
            if ch in string.punctuation:
                punctuation += ch
            else:
                words.append(punctuation)
                punctuation = ''
                words.append(' ')

    if word:
        words.append(word)
    if punctuation:
        words.append(punctuation)

    return ''.join(words[::-1])