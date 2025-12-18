"""
QUESTION:
Write a function named `find_pairs` that takes an array of integers `arr` and a target number `target` as input. The function should return all unique pairs of numbers in `arr` whose product equals `target`. The pairs should be stored in a new array, sorted in non-decreasing order, and should not contain any duplicate pairs. The function should handle duplicate numbers in `arr` correctly and have a time complexity of O(n^2) or better.
"""

def find_pairs(arr, target):
    pairs = []
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            product = arr[i] * arr[j]
            if product == target:
                new_pair = [arr[i], arr[j]]
                if new_pair not in pairs and new_pair[::-1] not in pairs:
                    pairs.append(new_pair)
    
    return pairs