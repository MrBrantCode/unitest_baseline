"""
QUESTION:
The purpose of this problem is to verify whether the method you are using to read input data is sufficiently fast to handle problems branded with the enormous Input/Output warning. You are expected to be able to process at least 2.5MB of input data per second at runtime.

-----Input-----
The input begins with two positive integers n k (n, k<=107). The next n lines of input contain one positive integer ti, not greater than 109, each.

-----Output-----
Write a single integer to output, denoting how many integers ti are divisible by k.

-----Example-----
Input:
7 3
1
51
966369
7
9
999996
11

Output:
4
"""

def count_divisible_numbers(n, k, numbers):
    """
    Counts how many integers in the list 'numbers' are divisible by 'k'.

    Parameters:
    n (int): The number of integers to be processed.
    k (int): The divisor to check against.
    numbers (list of int): A list of integers to be checked for divisibility by 'k'.

    Returns:
    int: The count of numbers in the list 'numbers' that are divisible by 'k'.
    """
    count = 0
    for number in numbers:
        if number % k == 0:
            count += 1
    return count