"""
QUESTION:
Given is an integer N. Find the number of digits that N has in base K.

-----Notes-----
For information on base-K representation, see Positional notation - Wikipedia.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N \leq 10^9
 - 2 \leq K \leq 10

-----Input-----
Input is given from Standard Input in the following format:
N K

-----Output-----
Print the number of digits that N has in base K.

-----Sample Input-----
11 2

-----Sample Output-----
4

In binary, 11 is represented as 1011.
"""

def count_digits_in_base(N: int, K: int) -> int:
    """
    Counts the number of digits that the integer N has in base K.

    Parameters:
    - N (int): The integer whose digits in base K are to be counted.
    - K (int): The base in which to count the digits of N.

    Returns:
    - int: The number of digits N has in base K.
    """
    if N == 0:
        return 1  # Special case: 0 has exactly one digit in any base
    
    digit_count = 0
    while N > 0:
        N //= K
        digit_count += 1
    
    return digit_count