"""
ORIGINAL QUESTION:
Write a function called `counting_sort` that sorts a list of integers without using comparisons. The function should take as input a list of integers and return a sorted list of integers. The function should only work for non-negative integers and should be efficient when the range of input values is small compared to the number of elements in the input list. The function should also handle cases where the input list is empty or contains duplicate values.
"""

def counting_sort(arr):
    """
    Sorts a list of non-negative integers using the counting sort algorithm.

    Args:
    arr (list): A list of non-negative integers.

    Returns:
    list: A sorted list of integers.
    """
    # Check if the input list is empty
    if not arr:
        return arr

    # Identify the range of input values
    min_val = min(arr)
    max_val = max(arr)

    # Create a counting array
    count_arr = [0] * (max_val - min_val + 1)

    # Count the frequencies
    for num in arr:
        count_arr[num - min_val] += 1

    # Calculate the cumulative counts
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Create the sorted output array
    sorted_arr = [0] * len(arr)

    # Traverse the input list in reverse order
    for num in reversed(arr):
        index = count_arr[num - min_val] - 1
        sorted_arr[index] = num
        count_arr[num - min_val] -= 1

    return sorted_arr