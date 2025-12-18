"""
QUESTION:
You are given a positive integer X.
Find the largest perfect power that is at most X.
Here, a perfect power is an integer that can be represented as b^p, where b is an integer not less than 1 and p is an integer not less than 2.

-----Constraints-----
 - 1 ≤ X ≤ 1000
 - X is an integer.

-----Input-----
Input is given from Standard Input in the following format:
X

-----Output-----
Print the largest perfect power that is at most X.

-----Sample Input-----
10

-----Sample Output-----
9

There are four perfect powers that are at most 10: 1, 4, 8 and 9.
We should print the largest among them, 9.
"""

def find_largest_perfect_power(X: int) -> int:
    """
    Finds the largest perfect power that is at most X.

    A perfect power is an integer that can be represented as b^p,
    where b is an integer not less than 1 and p is an integer not less than 2.

    Parameters:
    X (int): The upper limit (1 ≤ X ≤ 1000).

    Returns:
    int: The largest perfect power that is at most X.
    """
    perfect_powers = [1]
    for b in range(2, 32):
        num = 2
        while b ** num <= X:
            perfect_powers.append(b ** num)
            num += 1
    return max(perfect_powers)