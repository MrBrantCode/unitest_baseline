"""
QUESTION:
Create a function named `camouflage_text` that takes two parameters: `text` and `lexicon`. The function should replace all occurrences of the words in the `lexicon` list within the given `text` with a string of asterisks (*) of the same length as each word. The `lexicon` list contains specific words to be camouflaged and the function should return the modified text.
"""

def camouflage_text(text, lexicon):
    for word in lexicon:
        camouflage = '*' * len(word)
        text = text.replace(word, camouflage)
    return text