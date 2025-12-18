"""
QUESTION:
Create a function called `headline` that takes a string as input and returns the string in headline style, where the first word and major words are capitalized and minor words such as 'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'from', 'by' are in lowercase.
"""

def headline(title):
    words = title.split()
    small_words = ['a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'from', 'by']
    new_title = ''
    for i, w in enumerate(words):
        if i == 0 or w.lower() not in small_words:
            new_title += f'{w.capitalize()} '
        else:
            new_title += f'{w.lower()} '
    return new_title.strip()