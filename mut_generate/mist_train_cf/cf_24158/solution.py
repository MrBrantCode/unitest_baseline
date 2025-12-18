"""
QUESTION:
Write a function called `anagrams(word)` that returns all possible anagrams of the input string `word`. The function should be able to handle words of any length, and should not include duplicate anagrams in the output.
"""

def anagrams(word):
    if len(word) == 1:
        return [word]
    else:
        anagrams_list = []
        for i, letter in enumerate(word):
            for j in anagrams(word[:i]+word[i+1:]):
                anagrams_list.append(letter+j)
        return anagrams_list