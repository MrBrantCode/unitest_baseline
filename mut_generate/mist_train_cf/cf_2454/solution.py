"""
QUESTION:
Write a function named `can_form_word` that takes two parameters: a string `target_word` and a list of strings `word_list`. The function should return `True` if the `target_word` can be formed by concatenating two or more words from the `word_list` in the same order as they appear in the `word_list`, and `False` otherwise. The function should not use any built-in functions or libraries, should have a time complexity of O(n^2), and should not contain any spaces or special characters in the words or the target word.
"""

def can_form_word(target_word, word_list):
    n = len(target_word)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and target_word[j:i] in word_list:
                dp[i] = True
                break

    return dp[n]