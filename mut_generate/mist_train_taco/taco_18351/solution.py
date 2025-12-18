"""
QUESTION:
Fox Ciel is playing a game with numbers now. 

Ciel has n positive integers: x_1, x_2, ..., x_{n}. She can do the following operation as many times as needed: select two different indexes i and j such that x_{i} > x_{j} hold, and then apply assignment x_{i} = x_{i} - x_{j}. The goal is to make the sum of all numbers as small as possible.

Please help Ciel to find this minimal sum.


-----Input-----

The first line contains an integer n (2 ≤ n ≤ 100). Then the second line contains n integers: x_1, x_2, ..., x_{n} (1 ≤ x_{i} ≤ 100).


-----Output-----

Output a single integer — the required minimal sum.


-----Examples-----
Input
2
1 2

Output
2

Input
3
2 4 6

Output
6

Input
2
12 18

Output
12

Input
5
45 12 27 30 18

Output
15



-----Note-----

In the first example the optimal way is to do the assignment: x_2 = x_2 - x_1.

In the second example the optimal sequence of operations is: x_3 = x_3 - x_2, x_2 = x_2 - x_1.
"""

def minimal_sum_after_operations(n, arr):
    """
    Finds the minimal sum of the array after performing the allowed operations.

    Parameters:
    n (int): The number of elements in the array.
    arr (list of int): The array of integers.

    Returns:
    int: The minimal sum of the array after performing the allowed operations.
    """
    def findMaxSubarraySum(arr, n, sum):
        curr_sum = arr[0]
        max_sum = 0
        start = 0
        for i in range(1, n):
            if curr_sum <= sum:
                max_sum = max(max_sum, curr_sum)
            while curr_sum + arr[i] > sum and start < i:
                curr_sum -= arr[start]
                start += 1
            curr_sum += arr[i]
        if curr_sum <= sum:
            max_sum = max(max_sum, curr_sum)
        return max_sum
    
    arr = sorted(arr, reverse=True)
    while arr.count(arr[0]) != n:
        for i in range(n):
            arr[i] -= findMaxSubarraySum(arr, n, arr[i] - 1)
    
    return sum(arr)