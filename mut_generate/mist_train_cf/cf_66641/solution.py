"""
QUESTION:
Write two recursive functions, `traverse_words` and `traverse_characters`, where `traverse_words` takes a list of words and `traverse_characters` takes a word as input. The list of words can be deeply nested. The `traverse_characters` function should print each character of the word on a separate line, and `traverse_words` should return the total number of characters processed.
"""

def entance(wordList, count=0):
    for item in wordList:
        if isinstance(item, list):
            count = entance(item, count)
        else:
            count = traverse_characters(item, count)
    return count

def traverse_characters(word, count):
    for char in word:
        print(char)
        count += 1
    return count