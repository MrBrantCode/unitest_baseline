"""
QUESTION:
Create a function `get_sorted_unique_even_numbers` that takes an array of integers as input. The function should return a new array containing only the even numbers from the input array, sorted in ascending order and with no duplicates. If the input array is empty, the function should return an empty array. The solution should have a time complexity of O(n) and not use any additional data structures beyond the input and output arrays.
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