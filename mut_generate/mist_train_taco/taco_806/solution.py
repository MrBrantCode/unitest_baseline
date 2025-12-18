"""
QUESTION:
You are given an array a. Some element of this array a_{i} is a local minimum iff it is strictly less than both of its neighbours (that is, a_{i} < a_{i} - 1 and a_{i} < a_{i} + 1). Also the element can be called local maximum iff it is strictly greater than its neighbours (that is, a_{i} > a_{i} - 1 and a_{i} > a_{i} + 1). Since a_1 and a_{n} have only one neighbour each, they are neither local minima nor local maxima.

An element is called a local extremum iff it is either local maximum or local minimum. Your task is to calculate the number of local extrema in the given array.


-----Input-----

The first line contains one integer n (1 ≤ n ≤ 1000) — the number of elements in array a.

The second line contains n integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 1000) — the elements of array a.


-----Output-----

Print the number of local extrema in the given array.


-----Examples-----
Input
3
1 2 3

Output
0

Input
4
1 5 2 5

Output
2
"""

def count_local_extrema(arr: list) -> int:
    """
    Counts the number of local extrema in the given array.

    A local extremum is defined as an element that is either a local minimum or a local maximum.
    A local minimum is an element that is strictly less than both of its neighbors.
    A local maximum is an element that is strictly greater than both of its neighbors.
    The first and last elements of the array are not considered as they have only one neighbor.

    Parameters:
    arr (list): The array of integers to analyze.

    Returns:
    int: The number of local extrema in the array.
    """
    n = len(arr)
    if n < 3:
        return 0  # No local extrema possible if the array has less than 3 elements

    count = 0
    for i in range(1, n - 1):
        if (arr[i] < arr[i - 1] and arr[i] < arr[i + 1]) or (arr[i] > arr[i - 1] and arr[i] > arr[i + 1]):
            count += 1

    return count