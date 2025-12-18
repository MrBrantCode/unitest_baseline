"""
QUESTION:
Write a function `calculate_sum` that uses a recursive approach to calculate the sum of elements from a list of positive integers until a target sum is reached. The function should keep track of the number of iterations it takes to reach the target sum. The list should not exceed a length of 100 and the target sum should be a positive integer less than or equal to 1000. If the target sum is not reachable, the function should return an error message.
"""

def calculate_sum(numbers, target_sum, index=0, current_sum=0, iteration=0):
    if current_sum == target_sum:
        return iteration
    elif current_sum > target_sum or index >= len(numbers):
        return -1
    else:
        return calculate_sum(numbers, target_sum, index+1, current_sum+numbers[index], iteration+1)