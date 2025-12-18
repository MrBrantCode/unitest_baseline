"""
QUESTION:
A binary string is a string consisting only of the characters 0 and 1. You are given a binary string $s_1 s_2 \ldots s_n$. It is necessary to make this string non-decreasing in the least number of operations. In other words, each character should be not less than the previous. In one operation, you can do the following:

Select an arbitrary index $1 \leq i \leq n$ in the string;

For all $j \geq i$, change the value in the $j$-th position to the opposite, that is, if $s_j = 1$, then make $s_j = 0$, and vice versa.

What is the minimum number of operations needed to make the string non-decreasing?


-----Input-----

Each test consists of multiple test cases. The first line contains an integer $t$ ($1 \leq t \leq 10^4$) — the number of test cases. The description of test cases follows.

The first line of each test cases a single integer $n$ ($1 \leq n \leq 10^5$) — the length of the string.

The second line of each test case contains a binary string $s$ of length $n$.

It is guaranteed that the sum of $n$ over all test cases does not exceed $2 \cdot 10^5$.


-----Output-----

For each test case, output a single integer — the minimum number of operations that are needed to make the string non-decreasing.


-----Examples-----

Input
8
1
1
2
10
3
101
4
1100
5
11001
6
100010
10
0000110000
7
0101010
Output
0
1
2
1
2
3
1
5


-----Note-----

In the first test case, the string is already non-decreasing.

In the second test case, you can select $i = 1$ and then $s = \mathtt{01}$.

In the third test case, you can select $i = 1$ and get $s = \mathtt{010}$, and then select $i = 2$. As a result, we get $s = \mathtt{001}$, that is, a non-decreasing string.

In the sixth test case, you can select $i = 5$ at the first iteration and get $s = \mathtt{100001}$. Then choose $i = 2$, then $s = \mathtt{111110}$. Then we select $i = 1$, getting the non-decreasing string $s = \mathtt{000001}$.
"""

def min_operations_to_non_decreasing(binary_string: str) -> int:
    # Calculate the number of transitions between '0' and '1'
    k = sum((a != b for (a, b) in zip(binary_string, binary_string[1:])))
    
    # Calculate the additional operation if the string starts with '1' and contains '0'
    additional_operation = 1 if '0' in binary_string and binary_string[0] == '1' else 0
    
    # The minimum number of operations is the maximum of k - 1 or 0, plus any additional operation
    return max(k - 1, 0) + additional_operation