"""
QUESTION:
Write a function named `count_pairs` that takes three parameters: a list of positive integers, a target integer, and a threshold integer. The function should return the number of pairs of numbers in the list whose sum equals the target and whose difference is less than or equal to the threshold, without counting duplicate pairs.
"""

def count_pairs(numbers, target, threshold):
    count = 0
    pairs = set()
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) <= threshold and numbers[i] + numbers[j] == target:
                pairs.add((min(numbers[i], numbers[j]), max(numbers[i], numbers[j])))
    return len(pairs)