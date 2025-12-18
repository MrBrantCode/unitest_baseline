"""
QUESTION:
Create a function `find_anagrams(word)` that returns a list of all anagrams of the given word, with each anagram's length less than or equal to the length of the given word. The returned list should be in alphabetical order.
"""

def find_anagrams(word):
    if len(word) == 0:
        return []
    elif len(word) == 1:
        return [word]
    else:
        anagrams = []
        for i in range(len(word)):
            rest = word[:i] + word[i+1:]
            for perm in find_anagrams(rest):
                if len(word[i] + perm) <= len(word):
                    anagrams.append(word[i] + perm)
        return sorted(anagrams)