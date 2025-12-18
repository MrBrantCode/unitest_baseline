"""
QUESTION:
Create a function `underscore_punctuation(text)` that takes a string of text as input and returns a modified version of that text. The function uses a regular expression pattern to match different structures within the text and applies a substitution function to modify the text accordingly.

The regular expression pattern should match the following:

- Any alphanumeric character
- An underscore
- A space
- A parenthesis or quote
- A slash (to detect URLs)
- An HTML tag
- A URL
- Any non-space character

The substitution function should use a state dictionary to keep track of whether it is currently within a word or not. Based on this state, it should perform the following substitutions:

- If the match is within a word, return the original match
- If the match is an underscore and within a word, set the state to not within a word and return the original match
- If the match is a space and within a word, return a space
- If the match is a parenthesis or quote, set the state to not within a word and return the original match
- If the match is a URL or HTML tag, set the state to not within a word and return the original match
- For all other cases (mainly punctuation), set the state to not within a word and return the original match

The function should return the modified text after applying the substitution function to all matches in the input text.
"""

import re

def underscore_punctuation(text):
    state = {'within_word': False}

    pattern = r'''
    ([^\W_])              # any alphanumeric character
    | ([_])              # or an underscore
    | (\s)               # or a space
    | ([("\"'\[])        # or a parenthesis or quote
    | ([/])              # or a slash (to detect urls)
    | (<[^>]*>)          # or a HTML tag
    | (http[s]?://[^ ]*) # or a URL
    | ([^\s])            # or any non-space character
    '''

    def subfunc(m):
        if m.group(1):
            state['within_word'] = True
            return m.group(0)

        if m.group(2) and state['within_word']:
            state['within_word'] = False
            return m.group(0)

        if m.group(3) and state['within_word']:
            return ' '

        if m.group(4):
            state['within_word'] = False
            return m.group(0)

        if m.group(5):
            state['within_word'] = False
            return m.group(0)

        if m.group(6):
            state['within_word'] = False
            return m.group(0)

        if m.group(7):
            state['within_word'] = False
            return m.group(0)

        if m.group(8):
            state['within_word'] = False
            return m.group(0)

    return re.sub(pattern, subfunc, text, flags=re.VERBOSE)