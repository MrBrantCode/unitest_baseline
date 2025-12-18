"""
QUESTION:
Calculate the weighted average score of a list of numbers with their corresponding weights. The list can be empty and may contain negative, decimal, and repeated numbers. Weights can also be negative and decimal. The function should have a time complexity of O(n) and a space complexity of O(1). If the list is empty, return 0 as the weighted average score.

Function name: calculate_weighted_average
Input parameters: numbers (list of numbers), weights (list of corresponding weights)
Output: Weighted average score
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