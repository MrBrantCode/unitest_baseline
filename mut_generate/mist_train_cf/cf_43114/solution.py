"""
QUESTION:
Implement a function `calculate_total_similarities(strings)` that takes a list of strings as input and returns the total number of similarities found between all possible pairs of strings, where a similarity between two strings is defined as the number of positions at which the corresponding characters are the same. All strings in the input list are of the same length. The function should not compare a string with itself and should not compare a pair of strings more than once.
"""

def calculate_total_similarities(strings):
    total_similarities = 0
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            similarities = sum(a == b for a, b in zip(strings[i], strings[j]))
            total_similarities += similarities
    return total_similarities