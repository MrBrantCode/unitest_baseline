"""
QUESTION:
Write a function `find_joinable_pairs(words)` that takes a list of strings `words` and returns a list of tuples, where each tuple contains the indices of the joinable pair of words. Two words can be joined together if the last two characters of the first word are the same as the first two characters of the second word. The function should return all possible pairs if there are multiple joinable pairs, and an empty list if no joinable pairs are found.
"""

def find_joinable_pairs(words):
    joinable_pairs = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i][-2:] == words[j][:2]:
                joinable_pairs.append((i, j))
    return joinable_pairs