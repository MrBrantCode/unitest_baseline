"""
QUESTION:
Find any pair of words that are anagrams of each other in a given list of English words.

The function `find_anagrams(words)` should take a list of strings as input, where each string represents a word. It should return a list of tuples, where each tuple contains two words that are anagrams of each other.
"""

def find_anagrams(words):
    anagrams = [] 
    for i in range(len(words)): 
        for j in range(i+1, len(words)): 
            if (sorted(words[i]) == sorted(words[j])): 
                anagrams.append((words[i],words[j])) 
    return anagrams