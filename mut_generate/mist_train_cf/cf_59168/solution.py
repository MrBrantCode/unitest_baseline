"""
QUESTION:
Write a function `string_processing(s, targets, replaces)` that processes a string of words separated by white space or commas. The function should reformat the string into an array of words, preserving their initial sequence, and replace all instances of certain target words with fresh words provided as input. The function should take multiple targets and their corresponding replacements, where each target and replacement pair have the same index in their respective lists.
"""

def string_processing(s, targets, replaces):
    """
    This method processes a string of words, separated by white space or commas or a combination of both.
    It reformats this string into an array of words, preserving their initial sequence.
    After this, remove all instances of certain target words and replace them with fresh words provided as input.
    It can take multiple targets and their corresponding replacements.
    ARGS:
    s: input string to process
    targets: an array of words to replace
    replaces: an array of words that will replace targets correspondingly
    """

    words = s.replace(",", "").split()
    processed_words = []
    for word in words: 
        if word in targets: 
            word = replaces[targets.index(word)]
        processed_words.append(word)
    
    return processed_words