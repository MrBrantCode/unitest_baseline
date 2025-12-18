"""
QUESTION:
Alice gave Bob two integers $a$ and $b$ ($a > 0$ and $b \ge 0$). Being a curious boy, Bob wrote down an array of non-negative integers with $\operatorname{MEX}$ value of all elements equal to $a$ and $\operatorname{XOR}$ value of all elements equal to $b$.

What is the shortest possible length of the array Bob wrote?

Recall that the $\operatorname{MEX}$ ( Minimum EXcluded ) of an array is the minimum non-negative integer that does not belong to the array and the $\operatorname{XOR}$ of an array is the bitwise XOR of all the elements of the array.


-----Input-----

The input consists of multiple test cases. The first line contains an integer $t$ ($1 \leq t \leq 5 \cdot 10^4$) — the number of test cases. The description of the test cases follows.

The only line of each test case contains two integers $a$ and $b$ ($1 \leq a \leq 3 \cdot 10^5$; $0 \leq b \leq 3 \cdot 10^5$) — the $\operatorname{MEX}$ and $\operatorname{XOR}$ of the array, respectively.


-----Output-----

For each test case, output one (positive) integer — the length of the shortest array with $\operatorname{MEX}$ $a$ and $\operatorname{XOR}$ $b$. We can show that such an array always exists.


-----Examples-----

Input
5
1 1
2 1
2 0
1 10000
2 10000
Output
3
2
3
2
3


-----Note-----

In the first test case, one of the shortest arrays with $\operatorname{MEX}$ $1$ and $\operatorname{XOR}$ $1$ is $[0, 2020, 2021]$.

In the second test case, one of the shortest arrays with $\operatorname{MEX}$ $2$ and $\operatorname{XOR}$ $1$ is $[0, 1]$.

It can be shown that these arrays are the shortest arrays possible.
"""

def shortest_array_length(a: int, b: int) -> int:
    """
    Calculate the shortest possible length of an array with MEX value `a` and XOR value `b`.

    Parameters:
    a (int): The MEX value of the array (1 <= a <= 3 * 10^5).
    b (int): The XOR value of the array (0 <= b <= 3 * 10^5).

    Returns:
    int: The length of the shortest array with the given MEX and XOR values.
    """
    def computeXOR(n):
        if n % 4 == 0:
            return n
        if n % 4 == 1:
            return 1
        if n % 4 == 2:
            return n + 1
        return 0
    
    xor = computeXOR(a - 1)
    if xor == b:
        return a
    elif xor ^ a == b:
        return a + 2
    else:
        return a + 1