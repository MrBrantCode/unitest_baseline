"""
QUESTION:
Given a list of distinct words, write a function `find_palindrome_pairs(words)` that finds all distinct pairs of index values (i, j) such that the concatenation of the words at these indices (`words[i]` and `words[j]`) forms a palindrome word. The function should return a list of pairs of indices.
"""

def palindrome_pairs(words):
    def is_palindrome(check):
        return check == check[::-1]

    words = {word: i for i, word in enumerate(words)}
    valid_p = []

    for word, k in words.items():
        n = len(word)
        for j in range(n+1):
            pref = word[:j]
            suf = word[j:]
            if is_palindrome(pref):
                back = suf[::-1]
                if back != word and back in words:
                    valid_p.append([words[back],  k])
            if j !=n and is_palindrome(suf):
                back = pref[::-1]
                if back != word and back in words:
                    valid_p.append([k, words[back]])
    return valid_p