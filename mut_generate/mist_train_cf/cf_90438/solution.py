"""
QUESTION:
Implement a function `calculate_sum(arr, limit)` that takes an array of numbers and a given limit as input, and returns the sum of elements in the array that are divisible by 3, without exceeding the given limit. If there are no elements in the array that are divisible by 3, return -1. If the sum of the elements exceeds the given limit, return the sum of all elements that are divisible by 3 before the limit is exceeded.
"""

def calculate_sum(arr, limit):
    # Initialize the sum to 0
    sum = 0
    # Initialize a flag to check if there are elements divisible by 3
    divisible_by_3 = False

    # Iterate through the array
    for i in range(len(arr)):
        # Check if the element is divisible by 3
        if arr[i] % 3 == 0:
            # Add the element to the sum
            sum += arr[i]
            # Set the flag to True
            divisible_by_3 = True

            # Check if the sum exceeds the limit
            if sum > limit:
                # Subtract the current element from the sum
                sum -= arr[i]
                # Break the loop
                break

    # Check if there are elements divisible by 3
    if divisible_by_3:
        return sum
    else:
        return -1