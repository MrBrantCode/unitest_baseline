"""
QUESTION:
Write a function `find_increasing_subsequence` that takes a list of integers as input and returns `True` if there exists a strictly increasing subsequence of length 5 within the input numbers, and `False` otherwise. The input list is guaranteed to have more than 5 elements, and may contain duplicate numbers.
"""

def find_increasing_subsequence(numbers):
    n = len(numbers)
    if n < 5:
        return False

    # Create a list to store the lengths of increasing subsequences ending at each number
    lengths = [1] * n

    for i in range(1, n):
        for j in range(i):
            if numbers[i] > numbers[j] and lengths[i] < lengths[j] + 1:
                lengths[i] = lengths[j] + 1
                if lengths[i] >= 5:
                    return True

    return False