"""
QUESTION:
Write a function named `can_form_word` that takes a string `target_word` and a list of strings `word_list` as input, and returns a boolean indicating whether `target_word` can be formed by concatenating two or more words from `word_list` in the same order as they appear in `word_list`. Assume that the words in the list and the target word do not contain any spaces or special characters. The function should have a time complexity of O(n^2), where n is the length of the target word. Do not use any built-in functions or libraries to solve this problem.
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