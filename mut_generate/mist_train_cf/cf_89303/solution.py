"""
QUESTION:
Implement a function `extract_words(list_of_strings)` that extracts all the words that begin with 's' and end with 't' from the given list, while ignoring case sensitivity. The output should be a new list with the extracted words, and the order of the words in the output list should be the same as in the input list. The solution should have a time complexity of O(n^2), where n is the length of the input list, and a space complexity of O(m), where m is the number of words in the input list that satisfy the given condition.
"""

def entance(list_of_strings):
    extracted_words = []
    for word in list_of_strings:
        if word.lower().startswith('s') and word.lower().endswith('t'):
            extracted_words.append(word)
    return extracted_words