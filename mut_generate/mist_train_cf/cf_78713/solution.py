"""
QUESTION:
Create a function `solve_problem` that takes an array of mixed data types as input. The array may contain integers and non-integer values (e.g., strings, booleans). For each pair of consecutive integers in the array, calculate their sum. If the sum is a perfect square (i.e., the square root of the sum is an integer), consider it a valid entry; otherwise, it's non-valid. Return the count of valid and non-valid entries. Ignore non-integer values when forming pairs and calculating sums.
"""

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n

def entance(arr):
    valid, non_valid = 0, 0

    for i in range(len(arr) - 1):
        if isinstance(arr[i], int) and isinstance(arr[i + 1], int):
            sum_ = arr[i] + arr[i + 1]
            if is_perfect_square(sum_):
                valid += 1
            else:
                non_valid += 1

    return valid, non_valid