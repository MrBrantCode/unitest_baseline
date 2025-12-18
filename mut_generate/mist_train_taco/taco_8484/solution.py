"""
QUESTION:
In this Kata, you will be given two integers `n` and `k` and your task is to remove `k-digits` from `n` and return the lowest number possible, without changing the order of the digits in `n`. Return the result as a string.

Let's take an example of `solve(123056,4)`. We need to remove `4` digits from `123056` and return the lowest possible number. The best digits to remove are `(1,2,3,6)` so that the remaining digits are `'05'`. Therefore, `solve(123056,4) = '05'`. 

Note also that the order of the numbers in `n` does not change: `solve(1284569,2) = '12456',` because we have removed `8` and `9`. 

More examples in the test cases.

Good luck!
"""

from itertools import combinations

def remove_k_digits(n: int, k: int) -> str:
    """
    Removes k digits from the integer n and returns the smallest possible number as a string.

    Parameters:
    - n (int): The integer from which k digits will be removed.
    - k (int): The number of digits to remove from n.

    Returns:
    - str: The smallest possible number after removing k digits from n.
    """
    n_str = str(n)
    remaining_length = len(n_str) - k
    if remaining_length <= 0:
        return "0"
    
    # Generate all combinations of the digits of length remaining_length
    possible_combinations = combinations(n_str, remaining_length)
    
    # Find the minimum combination
    min_combination = min(possible_combinations)
    
    # Join the tuple into a string and return
    return ''.join(min_combination)