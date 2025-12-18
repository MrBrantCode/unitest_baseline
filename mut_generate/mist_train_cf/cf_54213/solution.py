"""
QUESTION:
Given a list of words, devise a Python function `palindrome_pairs` that returns all unique pairs of indices (i, j) such that the concatenation of words[i] and words[j] forms a palindrome, with the restriction that i and j are not equal.
"""

def palindrome_pairs(words):
    def is_palindrome(check):
        return check == check[::-1]

    words = {word: i for i, word in enumerate(words)}
    valid_pals = []

    for word, k in words.items():
        for j in range(len(word)+1):
            pref = word[:j]
            suf = word[j:]
            if is_palindrome(suf) and pref[::-1] in words and k != words[pref[::-1]]:
                valid_pals.append([k, words[pref[::-1]]])
            if j != len(word) and is_palindrome(pref) and suf[::-1] in words and k != words[suf[::-1]]:
                valid_pals.append([words[suf[::-1]], k])
    
    return valid_pals