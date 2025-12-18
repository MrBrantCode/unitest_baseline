"""
QUESTION:
In this kata, your task is to identify the pattern underlying a sequence of numbers. For example, if the sequence is [1, 2, 3, 4, 5], then the pattern is [1], since each number in the sequence is equal to the number preceding it, plus 1. See the test cases for more examples.

A few more rules :

pattern may contain negative numbers.
sequence will always be made of a whole number of repetitions of the pattern.
Your answer must correspond to the shortest form of the pattern, e.g. if the pattern is [1], then [1, 1, 1, 1] will not be considered a correct answer.
"""

from itertools import cycle

def identify_pattern(sequence):
    # Calculate the differences between consecutive elements
    diffs = [y - x for x, y in zip(sequence, sequence[1:])]
    
    # Find the shortest repeating pattern in the differences
    for i in range(1, len(diffs) + 1):
        if len(diffs) % i == 0 and all(a == b for a, b in zip(diffs, cycle(diffs[:i]))):
            return diffs[:i]
    
    # If no pattern is found, return an empty list (though the problem guarantees a pattern)
    return []