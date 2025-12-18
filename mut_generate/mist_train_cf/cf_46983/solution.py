"""
QUESTION:
Implement a function called `levenshtein(s1, s2)` to calculate the Levenshtein distance between two input strings `s1` and `s2`, which represents the minimum number of character edits (insertions, deletions, or substitutions) needed to transform `s1` into `s2`. The function should be efficient enough to handle a large number of string pairs, including English words, phrases, and sentences with possible variations, errors, extra whitespace, and punctuation.
"""

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]