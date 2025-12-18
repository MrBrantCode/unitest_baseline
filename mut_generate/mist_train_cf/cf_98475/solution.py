"""
QUESTION:
Write a function named `zero_sum_pairs` that takes a list of integers as input and returns a tuple containing a list of pairs of integers that add up to zero and the number of such pairs.
"""

def zero_sum_pairs(numbers):
    pairs = []
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == 0:
                pairs.append([numbers[i], numbers[j]])
                count += 1
    return pairs, count