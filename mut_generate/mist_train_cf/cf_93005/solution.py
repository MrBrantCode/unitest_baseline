"""
QUESTION:
Implement a recursive function `calculate_sum` that takes a list of positive integers `numbers` with a maximum length of 100 and a positive integer `target_sum` less than or equal to 1000 as input. The function should calculate the sum of the elements of the list using a while loop and return the number of iterations it takes to reach `target_sum`. If `target_sum` is not reachable with the given list, the function should return -1.
"""

def calculate_sum(numbers, target_sum, index=0, current_sum=0, iteration=0):
    if current_sum == target_sum:
        return iteration
    elif current_sum > target_sum or index >= len(numbers):
        return -1
    else:
        return calculate_sum(numbers, target_sum, index+1, current_sum+numbers[index], iteration+1)