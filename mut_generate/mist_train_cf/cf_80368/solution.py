"""
QUESTION:
Create a function `count_pairs(numbers, target_sum)` that takes a list of numbers and a target sum as input. The function should return the count of distinct pairs in the list whose cumulative total equals the target sum, with pairs (a, b) and (b, a) considered the same. The function must be implemented without using any pre-existing Python functions or libraries, and it should be efficient enough to handle large lists.
"""

def count_pairs(numbers, target_sum):
    count = 0
    seen = []

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            pair = sorted([numbers[i], numbers[j]])
            if sum(pair) == target_sum and pair not in seen:
                count += 1
                seen.append(pair)

    return count