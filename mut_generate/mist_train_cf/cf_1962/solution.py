"""
QUESTION:
Given a list of unique numbers and a target number, create a function `find_two_elements` that returns the indices of the two elements that sum to the target number with the smallest difference between the two elements. If no such pair exists, return an empty list. The function should have a time complexity of O(n log n) and the given solution's space complexity of O(n) is acceptable, although the original problem statement asked for O(1).
"""

def find_two_elements(numbers, target):
    numbers = sorted(enumerate(numbers), key=lambda x: x[1])  # Sort the numbers with their indices
    left = 0
    right = len(numbers) - 1
    min_diff = float('inf')
    result = []
    
    while left < right:
        current_sum = numbers[left][1] + numbers[right][1]
        
        if current_sum == target:
            diff = abs(numbers[left][1] - numbers[right][1])
            if diff < min_diff:
                min_diff = diff
                result = [numbers[left][0], numbers[right][0]]
        
        if current_sum < target:
            left += 1
        else:
            right -= 1
    
    return result