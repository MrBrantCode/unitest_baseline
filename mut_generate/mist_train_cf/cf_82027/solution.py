"""
QUESTION:
Implement a function `remove_recurring_elements` that takes a numerical array as input, removes any recurring elements, and returns the resulting array in ascending order. The solution should not use any direct array sorting functions. The input array may contain duplicate elements, and the output should only include unique elements that appear once in the input array.
"""

def remove_recurring_elements(arr):
    # Identify recurring elements by using a dictionary
    dictionary = {}
    for num in arr:
        if num in dictionary:
            dictionary[num] += 1
        else:
            dictionary[num] = 1

    # Remove recurring elements
    new_arr = [key for key, val in dictionary.items() if val == 1]

    # Sort the resultant array in ascending order using bubble sort
    for i in range(len(new_arr)):
        for j in range(i + 1, len(new_arr)):
            if new_arr[i] > new_arr[j]:
                # Swap
                new_arr[i], new_arr[j] = new_arr[j], new_arr[i]

    return new_arr