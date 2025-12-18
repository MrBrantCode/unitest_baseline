"""
QUESTION:
You are given $n$ integers $a_1, a_2, \ldots, a_n$. You choose any subset of the given numbers (possibly, none or all numbers) and negate these numbers (i. e. change $x \to (-x)$). What is the maximum number of different values in the array you can achieve?


-----Input-----

The first line of input contains one integer $t$ ($1 \leq t \leq 100$): the number of test cases.

The next lines contain the description of the $t$ test cases, two lines per a test case.

In the first line you are given one integer $n$ ($1 \leq n \leq 100$): the number of integers in the array.

The second line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($-100 \leq a_i \leq 100$).


-----Output-----

For each test case, print one integer: the maximum number of different elements in the array that you can achieve negating numbers in the array.


-----Examples-----

Input
3
4
1 1 2 2
3
1 2 3
2
0 0
Output
4
3
1


-----Note-----

In the first example we can, for example, negate the first and the last numbers, achieving the array $[-1, 1, 2, -2]$ with four different values.

In the second example all three numbers are already different.

In the third example negation does not change anything.
"""

def max_different_values(arr: list) -> int:
    """
    Calculate the maximum number of different values in the array that can be achieved by negating any subset of the given numbers.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The maximum number of different values that can be achieved.
    """
    unique_values = set()
    for num in arr:
        if num in unique_values:
            unique_values.add(-num)
        else:
            unique_values.add(num)
    return len(unique_values)