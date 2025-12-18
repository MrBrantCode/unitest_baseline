"""
QUESTION:
Write a function `can_form_word(target_word, word_list)` that determines if the target word can be formed by concatenating two or more words from the word list. The concatenation must be in the same order as the words in the list. The function should have a time complexity of O(n^2), where n is the length of the target word, and should not use any built-in functions or libraries.
"""

def can_form_word(target_word, word_list):
    # Create a list to keep track of whether a word can be formed at each index of the target word
    can_form = [False] * (len(target_word) + 1)
    # The empty string can always be formed
    can_form[0] = True

    # Iterate through each index of the target word
    for i in range(1, len(target_word) + 1):
        # Check if the current substring of the target word can be formed by concatenating words from the list
        for j in range(i):
            # If the substring from j to i can be formed and the word from j to i is in the list,
            # mark that the substring from 0 to i can be formed
            if can_form[j] and target_word[j:i] in word_list:
                can_form[i] = True
                break

    # Return whether the entire target word can be formed
    return can_form[len(target_word)]