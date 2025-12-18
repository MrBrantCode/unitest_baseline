"""
QUESTION:
Write a function `findPairs(numbers, targetSum)` that takes a list of numbers and a target sum as input, and prints out all pairs of numbers whose sum is equal to the target sum. The output should be sorted in ascending order of the first number in each pair, and the order of the numbers in the pair should not matter. The function should be optimized to have a time complexity of O(n), where n is the length of the input array.
"""

def findPairs(numbers, targetSum):
    pairs = []
    seen = set()
    
    for num in numbers:
        complement = targetSum - num
        if complement in seen:
            pair = (min(num, complement), max(num, complement))
            pairs.append(pair)
        seen.add(num)
    
    pairs.sort()
    return pairs