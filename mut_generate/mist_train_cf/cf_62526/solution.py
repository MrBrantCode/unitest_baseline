"""
QUESTION:
Develop a function `find_word` that takes a 2D list of strings `data` and a target string `target` as input. The function should return the frequency of the target string in the 2D list and its positions (as tuples of indices of the sublist and the index of the word within the sublist). The target string may appear multiple times in the 2D list.
"""

def find_word(data, target):
    frequency = 0
    positions = []

    for i, sublist in enumerate(data):
        for j, word in enumerate(sublist):
            if word == target:
                positions.append((i, j))
            frequency += word.count(target)

    return frequency, positions