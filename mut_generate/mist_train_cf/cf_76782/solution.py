"""
QUESTION:
Write a function named `print_chars` that takes a list of words and uses recursion to print each character from every word on a distinct line. The function should have two optional parameters, `wordIndex` and `charIndex`, with default values of 0. Ensure the function has clear and concise comments explaining the recursion steps.
"""

def print_chars(wordList, wordIndex=0, charIndex=0):
    # base case: if we've processed all words, do nothing (just return)
    if wordIndex >= len(wordList):
        return
    # base case: if we've processed all characters of the current word, move on to the next word
    if charIndex >= len(wordList[wordIndex]):
        print_chars(wordList, wordIndex + 1, 0)
    else:
        # recursive case: print the current character and recurse for the rest of the characters of the current word
        print(wordList[wordIndex][charIndex])
        print_chars(wordList, wordIndex,  charIndex + 1)