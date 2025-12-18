"""
QUESTION:
Create a function named `count_word_occurrences` that takes two parameters: `myString` and `word`. The function should count the occurrences of `word` in `myString`, considering only consecutive lowercase alphabetical characters and ignoring case sensitivity. The function should return the count of occurrences if the word is found at least once, and -1 otherwise. The implementation must achieve a time complexity of O(n), where n is the length of `myString`, and a space complexity of O(1), without using built-in string matching or regular expression functions.
"""

def count_word_occurrences(myString, word):
    count = 0
    word_length = len(word)
    i = 0
    
    while i < len(myString):
        if myString[i].islower():
            j = 0
            while j < word_length and i + j < len(myString) and myString[i + j].islower():
                if myString[i + j].lower() != word[j].lower():
                    break
                j += 1
            
            if j == word_length:
                count += 1
                i += word_length
            else:
                i += 1
        else:
            i += 1
    
    if count > 0:
        return count
    else:
        return -1