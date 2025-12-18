"""
QUESTION:
We ask you to select some number of positive integers, and calculate the sum of them.
It is allowed to select as many integers as you like, and as large integers as you wish.
You have to follow these, however: each selected integer needs to be a multiple of A, and you need to select at least one integer.
Your objective is to make the sum congruent to C modulo B.
Determine whether this is possible.
If the objective is achievable, print YES. Otherwise, print NO.

-----Constraints-----
 - 1 ≤ A ≤ 100
 - 1 ≤ B ≤ 100
 - 0 ≤ C < B

-----Input-----
Input is given from Standard Input in the following format:
A B C

-----Output-----
Print YES or NO.

-----Sample Input-----
7 5 1

-----Sample Output-----
YES

For example, if you select 7 and 14, the sum 21 is congruent to 1 modulo 5.
"""

def is_sum_congruent_to_c_modulo_b(A: int, B: int, C: int) -> str:
    """
    Determines whether it is possible to select some number of positive integers,
    each being a multiple of A, such that their sum is congruent to C modulo B.

    Parameters:
    - A (int): The base integer whose multiples are considered.
    - B (int): The modulus for the congruence check.
    - C (int): The target remainder when the sum is divided by B.

    Returns:
    - str: "YES" if the objective is achievable, otherwise "NO".
    """
    for i in range(1, B + 1):
        if i * A % B == C:
            return 'YES'
    return 'NO'