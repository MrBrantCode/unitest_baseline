"""
QUESTION:
Write a recursive function `word_processing(wordList, alphaCount = {}, index = 0)` that takes a list of words `wordList` and two optional parameters `alphaCount` (a dictionary to store the count of unique alphabets) and `index` (the current index in the list). The function should print the ASCII representation of each letter in each word on a separate line and return the count of unique alphabets across all words. Consider all words to be case sensitive.
"""

def word_processing(wordList, alphaCount = {}, index = 0):
    # Base case: if list is empty, return count of unique alphabets
    if index == len(wordList):
        return len(alphaCount)

    # Process each word
    for letter in wordList[index]:
        print(ord(letter))  # Print ASCII representation
        alphaCount[letter] = alphaCount.get(letter, 0) + 1  # Keep count of unique alphabets

    # Recursive call for next word
    return word_processing(wordList, alphaCount, index + 1)