"""
QUESTION:
Create a function `get_sorted_unique_even_numbers` that takes an array of integers as input and returns a new array containing only the unique even numbers in ascending order. If the input array is empty, the function should return an empty array. The function should have a time complexity of O(n) and not use any additional data structures other than the output array.
"""

def get_sorted_unique_even_numbers(arr):
    if len(arr) == 0:
        return []

    count = 0
    for num in arr:
        if num % 2 == 0:
            count += 1

    result = [0] * count
    index = 0
    for num in arr:
        if num % 2 == 0:
            result[index] = num
            index += 1

    # Bubble Sort
    for i in range(len(result)):
        for j in range(len(result) - 1 - i):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]

    # Remove duplicates
    i = 0
    while i < len(result) - 1:
        if result[i] == result[i+1]:
            result.pop(i+1)
        else:
            i += 1

    return result