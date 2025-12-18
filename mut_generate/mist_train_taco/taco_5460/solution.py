"""
QUESTION:
You are given an array $a$ consisting of $n$ integers.

Let's call a pair of indices $i$, $j$ good if $1 \le i < j \le n$ and $\gcd(a_i, 2a_j) > 1$ (where $\gcd(x, y)$ is the greatest common divisor of $x$ and $y$).

Find the maximum number of good index pairs if you can reorder the array $a$ in an arbitrary way.


-----Input-----

The first line contains a single integer $t$ ($1 \le t \le 1000$) — the number of test cases.

The first line of the test case contains a single integer $n$ ($2 \le n \le 2000$) — the number of elements in the array.

The second line of the test case contains $n$ integers $a_1, a_2, \dots, a_n$ ($1 \le a_i \le 10^5$).

It is guaranteed that the sum of $n$ over all test cases does not exceed $2000$.


-----Output-----

For each test case, output a single integer — the maximum number of good index pairs if you can reorder the array $a$ in an arbitrary way.


-----Examples-----

Input
3
4
3 6 5 3
2
1 7
5
1 4 2 4 1
Output
4
0
9


-----Note-----

In the first example, the array elements can be rearranged as follows: $[6, 3, 5, 3]$.

In the third example, the array elements can be rearranged as follows: $[4, 4, 2, 1, 1]$.
"""

from math import gcd

def max_good_index_pairs(a):
    """
    Calculate the maximum number of good index pairs in the array `a` if it can be reordered in an arbitrary way.

    A pair of indices (i, j) is considered good if 1 <= i < j <= n and gcd(a_i, 2 * a_j) > 1.

    Parameters:
    a (list of int): The array of integers.

    Returns:
    int: The maximum number of good index pairs.
    """
    res = 0
    one = 0
    even = 0
    nums = []

    # Separate the elements into different categories
    for num in a:
        if num == 1:
            one += 1
        elif num % 2 == 0:
            even += 1
        else:
            nums.append(num)

    n = len(nums)

    # Calculate pairs involving 1s and evens
    res += one * even

    # Calculate pairs involving evens and the rest of the numbers
    res += even * n

    # Calculate pairs among evens themselves
    res += sum(range(even))

    # Calculate pairs among the remaining numbers
    while nums:
        num = nums.pop()
        res += len([1 for i in nums if gcd(num, i) > 1])

    return res