"""
QUESTION:
Given a list of words and a pattern, implement the function `findAndReplacePattern(words, pattern)` to find and return the words that match the given pattern. A word matches the pattern if there exists a permutation of letters `p` so that after replacing every letter `x` in the pattern with `p(x)`, we get the desired word, and the sum of the ASCII values of the original letters is equal to the sum of the ASCII values of the replaced letters. The function may return the answer in any order. The length of `words` is between 1 and 50, and the length of each word and the pattern is between 1 and 20.
"""

def findAndReplacePattern(words, pattern):
    def match(word):
        m1, m2 = {}, {}
        for w, p in zip(word, pattern):
            if w not in m1: m1[w] = p
            if p not in m2: m2[p] = w
            if (m1[w], m2[p]) != (p, w):
                return False
        return True

    return [w for w in words if match(w)]