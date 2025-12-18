"""
QUESTION:
Thanos sort is a supervillain sorting algorithm, which works as follows: if the array is not sorted, snap your fingers* to remove the first or the second half of the items, and repeat the process.

Given an input array, what is the size of the longest sorted array you can obtain from it using Thanos sort?

*Infinity Gauntlet required.


-----Input-----

The first line of input contains a single number $n$ ($1 \le n \le 16$) — the size of the array. $n$ is guaranteed to be a power of 2.

The second line of input contains $n$ space-separated integers $a_i$ ($1 \le a_i \le 100$) — the elements of the array.


-----Output-----

Return the maximal length of a sorted array you can obtain using Thanos sort. The elements of the array have to be sorted in non-decreasing order.


-----Examples-----
Input
4
1 2 2 4

Output
4

Input
8
11 12 1 2 13 14 3 4

Output
2

Input
4
7 6 5 4

Output
1



-----Note-----

In the first example the array is already sorted, so no finger snaps are required.

In the second example the array actually has a subarray of 4 sorted elements, but you can not remove elements from different sides of the array in one finger snap. Each time you have to remove either the whole first half or the whole second half, so you'll have to snap your fingers twice to get to a 2-element sorted array.

In the third example the array is sorted in decreasing order, so you can only save one element from the ultimate destruction.
"""

def is_sorted(array):
    """Helper function to check if the array is sorted in non-decreasing order."""
    for i in range(len(array) - 1):
        if array[i + 1] < array[i]:
            return False
    return True

def thanos_sort_length(array):
    """
    Returns the maximal length of a sorted array that can be obtained using Thanos sort.
    
    Parameters:
    array (list of int): The input array to be sorted.
    
    Returns:
    int: The maximal length of a sorted array.
    """
    n = len(array)
    
    if n == 1:
        return 1
    elif is_sorted(array):
        return n
    else:
        # Split the array into two halves
        first_half = array[:n // 2]
        second_half = array[n // 2:]
        
        # Recursively apply Thanos sort to both halves
        length_first_half = thanos_sort_length(first_half)
        length_second_half = thanos_sort_length(second_half)
        
        # Return the maximum length of the sorted subarrays
        return max(length_first_half, length_second_half)