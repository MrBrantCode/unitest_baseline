"""
QUESTION:
Write a function named `three_sum` that takes a list of integers `arr` and an integer `target` as input. The function should return a list of unique triplets in `arr` that sum up to `target`. The input list can contain duplicate values and may not be sorted. The function should return an empty list if no such triplet exists. The solution should have a time complexity of O(n^2), where n is the length of `arr`.
"""

def three_sum(arr, target):
    arr.sort()
    solutions = []
    n = len(arr)
    for i in range(n-2):
        left = i+1
        right = n-1
        while left < right:
            if arr[i] + arr[left] + arr[right] == target:
                if sorted([arr[i], arr[left], arr[right]]) not in solutions: 
                    solutions.append(sorted([arr[i], arr[left], arr[right]]))
                left += 1 
                right -= 1
            elif arr[i] + arr[left] + arr[right] < target:
                left += 1
            else:
                right -= 1
    return solutions