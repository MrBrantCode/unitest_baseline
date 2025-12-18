"""
QUESTION:
Given a sequence of `words` written in an alien language, the `order` of the alphabet, and an integer `n`, write a function `isAlienSorted` that returns `true` if and only if the given `words` are sorted lexicographically in this alien language and the same letter does not appear more than `n` times consecutively in a word. The function should take three parameters: `words`, `order`, and `n`. The function must satisfy the following constraints: 
`1 <= len(words) <= 100`, `1 <= len(word) <= 20` for each `word` in `words`, `len(order) == 26`, and `1 <= n <= 20`. All characters in `words` and `order` are English lowercase letters.
"""

def isAlienSorted(words, order, n):
    order_dict = {char: i for i, char in enumerate(order)}

    for word in words:
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                count += 1
            else:
                count = 1
            if count > n:
                return False

    for i in range(len(words)-1):
        word1 = words[i]
        word2 = words[i+1]

        for j in range(min(len(word1), len(word2))):
            if word1[j] != word2[j]:
                if order_dict[word1[j]] > order_dict[word2[j]]:
                    return False
                break
        else:
            if len(word1) > len(word2):
                return False

    return True