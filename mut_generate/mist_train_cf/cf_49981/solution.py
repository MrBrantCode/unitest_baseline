"""
QUESTION:
Develop a function called `check_progression` that accepts a numeric array as input. The function should determine if the array adheres to an ascending progression and return a boolean indicating whether the array is a progression and the common difference of the progression if it exists. The function should work for arrays with at least two elements and handle both integer and floating point numbers. The time complexity of the function should be efficient enough to handle large-sized arrays.
"""

def check_progression(arr):
    # Assert that the array has at least 2 elements
    if len(arr) < 2:
        return False

    # Calculate the difference between the first two numbers
    common_difference = arr[1] - arr[0]

    # Iterate through the array to check if the remaining elements meet the progression requirements
    for i in range(len(arr) - 1):
        # Check if difference between current and next number is equal to common difference
        if arr[i+1] - arr[i] != common_difference:
            # If not, return False
            return False
            
    # If all checks passed, return True and the common difference
    return True, common_difference