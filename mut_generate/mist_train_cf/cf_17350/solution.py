"""
QUESTION:
Write a function `can_form_word(target_word, word_list)` that determines if the `target_word` can be formed by concatenating two or more words from the `word_list` in the same order. The words in the `word_list` and the `target_word` do not contain any spaces or special characters. The function should have a time complexity of O(n^2), where n is the length of the `target_word`.
"""

def can_form_word(target_word, word_list):
    can_form = [False] * (len(target_word) + 1)
    can_form[0] = True

    for i in range(1, len(target_word) + 1):
        for j in range(i):
            if can_form[j] and target_word[j:i] in word_list:
                can_form[i] = True
                break

    return can_form[len(target_word)]