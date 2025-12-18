"""
QUESTION:
Given an array of unique lower-case English words, find all pairs of distinct indices `(i, j)` such that the concatenation `words[i] + words[j]` is a palindrome. The length of the array is between 1 and 5000 inclusive, and the length of each word is between 1 and 20 inclusive. Implement a function `palindromePairs` that returns a list of these pairs.
"""

def palindromePairs(words):
    def is_palindrome(check):
        return check == check[::-1]

    words = {word: i for i, word in enumerate(words)}
    valid_pals = []
    for word, k in words.items():
        n = len(word)
        for j in range(n+1):
            pref = word[:j]
            suf = word[j:]
            if is_palindrome(pref):
                back = suf[::-1]
                if back != word and back in words:
                    valid_pals.append([words[back],  k])
            if j != n and is_palindrome(suf):
                back = pref[::-1]
                if back != word and back in words:
                    valid_pals.append([k, words[back]])
    return valid_pals