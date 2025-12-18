"""
QUESTION:
Create a function `quad_combinations(num_sequence)` that generates all possible combinations of multiplying three numbers from the given sequence. The sequence can contain duplicates, and the same number can be used multiple times in one combination. The function should return a list of all possible combinations. The input sequence will contain at least one number.
"""

def quad_combinations(num_sequence):
    result = []
    length = len(num_sequence)
    for i in range(length):
        for j in range(length):
            for k in range(length):
                result.append(num_sequence[i]*num_sequence[j]*num_sequence[k])
    return result