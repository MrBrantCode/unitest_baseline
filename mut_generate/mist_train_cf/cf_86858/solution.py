"""
QUESTION:
Create a function `filter_positive_greater_than_10` that takes an array of integers as input and returns a new array containing only the positive numbers greater than 10 in ascending order, without using any built-in Python functions or libraries for sorting. The function should have a time complexity of O(n log n).
"""

def filter_positive_greater_than_10(arr):
    filtered_array = []
    for num in arr:
        if num > 10 and num > 0:
            filtered_array.append(num)

    for i in range(len(filtered_array)):
        for j in range(i+1, len(filtered_array)):
            if filtered_array[i] > filtered_array[j]:
                filtered_array[i], filtered_array[j] = filtered_array[j], filtered_array[i]
    return filtered_array