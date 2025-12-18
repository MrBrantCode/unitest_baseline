"""
QUESTION:
Quan_Lank loves awsome numbers. Awsome numbers are the positive integers whose decimal representations contain only the awsome digits 4 and 7. For example, numbers 7, 74, 4 are awsome and 5, 137, 4467 are not. Unfortunately, not all numbers are awsome. Quan_Lank calls a number nearly awsome if the number of awsome digits in it is a awsome number. He wonders whether number n is a nearly awsome number.

INPUT :

First line of Input contains no. of test cases T(T ≤ 100).
Each test case contains one line having a single integer n (1 ≤ n ≤ 10^18).

OUTPUT :

For each test case print on the single line "YES" if n is a nearly awsome number. Otherwise, print "NO" (without the quotes).

SAMPLE INPUT
2
40047
4777

SAMPLE OUTPUT
NO
YES
"""

def is_nearly_awesome(n: int) -> str:
    """
    Determines if a given number n is a nearly awesome number.

    A number is nearly awesome if the count of awesome digits (4 and 7) in its decimal representation
    is itself an awesome number.

    Parameters:
    n (int): The number to be checked.

    Returns:
    str: "YES" if n is a nearly awesome number, otherwise "NO".
    """
    def is_awesome(num: int) -> bool:
        """Helper function to check if a number is an awesome number."""
        num_str = str(num)
        for digit in num_str:
            if digit != '4' and digit != '7':
                return False
        return True

    n_str = str(n)
    awesome_count = sum(1 for digit in n_str if digit == '4' or digit == '7')
    
    if is_awesome(awesome_count):
        return "YES"
    else:
        return "NO"