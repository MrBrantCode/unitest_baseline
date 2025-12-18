"""
QUESTION:
Create a function called `calculate_weighted_average` that takes two lists as input: `numbers` and `weights`. The function should calculate the weighted average of the numbers, where each number is weighted by the corresponding value in the `weights` list. The function should handle the following conditions: the lists may be empty, may contain negative or decimal numbers, may contain repeated numbers and weights, and may have a large number of elements. The weights may be negative or decimal. The function should have a time complexity of O(n), where n is the number of elements in the list, and a space complexity of O(1). If the list is empty, return 0 as the weighted average score.
"""

def calculate_weighted_average(numbers, weights):
    if len(numbers) == 0:
        return 0
    
    weighted_sum = 0
    total_weight = 0
    
    for i in range(len(numbers)):
        weighted_sum += numbers[i] * weights[i]
        total_weight += weights[i]
    
    weighted_average = weighted_sum / total_weight
    return weighted_average