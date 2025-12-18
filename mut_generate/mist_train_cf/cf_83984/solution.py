"""
QUESTION:
Create a function named `sort_words` that takes a list of words and a criterion function as input. The function should sort the list of words based on the given criterion. In case of a tie between words of the same length, the function should sort the words in descending order based on their ASCII value. The function should return an error message "Invalid input" if the input list or any element in the list is `None`.
"""

def sort_words(words, criterion):
    if words == None or any(word is None for word in words):
        return "Invalid input"
    else:
        return sorted([word for word in words if criterion(word)], key = lambda x: (len(x), x), reverse = True)