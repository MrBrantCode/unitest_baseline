"""
QUESTION:
Given three distinct integers $a$, $b$, and $c$, find the medium number between all of them.

The medium number is the number that is neither the minimum nor the maximum of the given three numbers.

For example, the median of $5,2,6$ is $5$, since the minimum is $2$ and the maximum is $6$.


-----Input-----

The first line contains a single integer $t$ ($1 \leq t \leq 6840$) — the number of test cases.

The description of each test case consists of three distinct integers $a$, $b$, $c$ ($1 \leq a, b, c \leq 20$).


-----Output-----

For each test case, output a single integer — the medium number of the three numbers.


-----Examples-----

Input
9
5 2 6
14 3 4
20 2 1
1 2 3
11 19 12
10 8 20
6 20 3
4 1 3
19 8 4
Output
5
4
2
2
12
10
6
3
8


-----Note-----

None
"""

def find_median(a: int, b: int, c: int) -> int:
    """
    Find the median number among three distinct integers.

    Parameters:
    a (int): The first distinct integer.
    b (int): The second distinct integer.
    c (int): The third distinct integer.

    Returns:
    int: The median number among the three integers.
    """
    # Sort the three numbers
    sorted_numbers = sorted([a, b, c])
    # The median is the second element in the sorted list
    return sorted_numbers[1]