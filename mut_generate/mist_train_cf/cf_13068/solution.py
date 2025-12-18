"""
QUESTION:
Find all pairs of numbers in an array that add up to a target number N. Create a function named `find_pairs` that takes two parameters: an array of integers and the target number N, and returns a list of pairs of numbers that add up to N. The function should return all possible pairs.
"""

def find_pairs(array, N):
    pairs = set()
    result = []
    for num in array:
        diff = N - num
        if diff in pairs:
            result.append([diff, num])
        pairs.add(num)
    return result