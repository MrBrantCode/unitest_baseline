"""
QUESTION:
Given is an integer N. Find the number of positive integers less than or equal to N that have an odd number of digits (in base ten without leading zeros).

-----Constraints-----
 - 1 \leq N \leq 10^5

-----Input-----
Input is given from Standard Input in the following format:
N

-----Output-----
Print the number of positive integers less than or equal to N that have an odd number of digits.

-----Sample Input-----
11

-----Sample Output-----
9

Among the positive integers less than or equal to 11, nine integers have an odd number of digits: 1, 2, \ldots, 9.
"""

def count_odd_digit_numbers(N: int) -> int:
    """
    Counts the number of positive integers less than or equal to N that have an odd number of digits.

    Parameters:
    N (int): The upper limit (inclusive) up to which to count the numbers.

    Returns:
    int: The count of positive integers with an odd number of digits.
    """
    ans = 0
    for i in range(1, N + 1):
        if len(str(i)) % 2 == 1:
            ans += 1
    return ans