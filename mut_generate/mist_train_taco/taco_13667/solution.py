"""
QUESTION:
Polycarp likes squares and cubes of positive integers. Here is the beginning of the sequence of numbers he likes: $1$, $4$, $8$, $9$, ....

For a given number $n$, count the number of integers from $1$ to $n$ that Polycarp likes. In other words, find the number of such $x$ that $x$ is a square of a positive integer number or a cube of a positive integer number (or both a square and a cube simultaneously).


-----Input-----

The first line contains an integer $t$ ($1 \le t \le 20$) — the number of test cases.

Then $t$ lines contain the test cases, one per line. Each of the lines contains one integer $n$ ($1 \le n \le 10^9$).


-----Output-----

For each test case, print the answer you are looking for — the number of integers from $1$ to $n$ that Polycarp likes.


-----Examples-----

Input
6
10
1
25
1000000000
999999999
500000000
Output
4
1
6
32591
32590
23125


-----Note-----

None
"""

def count_polycarp_likes(n: int) -> int:
    """
    Counts the number of integers from 1 to n that are either squares or cubes (or both) of positive integers.

    Parameters:
    n (int): The upper limit of the range from 1 to n (inclusive).

    Returns:
    int: The count of numbers from 1 to n that Polycarp likes.
    """
    return int(n ** 0.5) + int(n ** (1 / 3)) - int(n ** (1 / 6))