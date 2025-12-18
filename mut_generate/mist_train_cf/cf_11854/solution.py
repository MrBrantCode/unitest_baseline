"""
QUESTION:
Convert the numeric string elements in a given array to integers, excluding non-numeric strings, and return them in a new array sorted in descending order without using any built-in sorting functions or libraries.

Function name: convert_and_sort

Input: An array of strings
Output: An array of integers
Restriction: Do not use built-in sorting functions or libraries.
"""

def convert_and_sort(arr):
    """
    Converts numeric string elements in a given array to integers, 
    excluding non-numeric strings, and returns them in a new array 
    sorted in descending order without using any built-in sorting functions or libraries.
    
    Parameters:
    arr (list): An array of strings
    
    Returns:
    list: An array of integers
    """
    converted_nums = []
    for num in arr:
        try:
            converted_nums.append(int(num))
        except ValueError:
            continue

    # Bubble sort in descending order
    n = len(converted_nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if converted_nums[j] < converted_nums[j+1]:
                converted_nums[j], converted_nums[j+1] = converted_nums[j+1], converted_nums[j]

    return converted_nums