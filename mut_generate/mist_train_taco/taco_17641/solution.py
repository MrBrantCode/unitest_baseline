"""
QUESTION:
Ksusha is a beginner coder. Today she starts studying arrays. She has array a_1, a_2, ..., a_{n}, consisting of n positive integers.

Her university teacher gave her a task. Find such number in the array, that all array elements are divisible by it. Help her and find the number!


-----Input-----

The first line contains integer n (1 ≤ n ≤ 10^5), showing how many numbers the array has. The next line contains integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 10^9) — the array elements.


-----Output-----

Print a single integer — the number from the array, such that all array elements are divisible by it. If such number doesn't exist, print -1.

If there are multiple answers, you are allowed to print any of them.


-----Examples-----
Input
3
2 2 4

Output
2

Input
5
2 1 3 1 6

Output
1

Input
3
2 3 5

Output
-1
"""

def find_divisible_number(arr):
    """
    Finds a number in the array such that all array elements are divisible by it.
    
    Parameters:
    arr (list of int): The array of positive integers.
    
    Returns:
    int: The number from the array such that all array elements are divisible by it,
         or -1 if no such number exists.
    """
    set_arr = set(arr)
    result = -1
    
    for i in set_arr:
        if all(j % i == 0 for j in set_arr):
            result = i
            break
    
    return result