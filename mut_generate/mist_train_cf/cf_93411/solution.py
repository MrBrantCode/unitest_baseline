"""
QUESTION:
Write a function named `calculate_sum_within_limit` that takes two parameters: an array of numbers and a limit. The function should use a nested loop to calculate the sum of elements in the array, and it should only add elements to the sum if doing so does not exceed the given limit. The function should return the calculated sum.
"""

def calculate_sum_within_limit(arr, limit):
    sum = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if sum + arr[j] <= limit:
                sum += arr[j]
            else:
                break
    return sum