"""
QUESTION:
Gottfried learned about binary number representation. He then came up with this task and presented it to you.

You are given a collection of $n$ non-negative integers $a_1, \ldots, a_n$. You are allowed to perform the following operation: choose two distinct indices $1 \leq i, j \leq n$. If before the operation $a_i = x$, $a_j = y$, then after the operation $a_i = x~\mathsf{AND}~y$, $a_j = x~\mathsf{OR}~y$, where $\mathsf{AND}$ and $\mathsf{OR}$ are bitwise AND and OR respectively (refer to the Notes section for formal description). The operation may be performed any number of times (possibly zero).

After all operations are done, compute $\sum_{i=1}^n a_i^2$ — the sum of squares of all $a_i$. What is the largest sum of squares you can achieve?


-----Input-----

The first line contains a single integer $n$ ($1 \leq n \leq 2 \cdot 10^5$).

The second line contains $n$ integers $a_1, \ldots, a_n$ ($0 \leq a_i < 2^{20}$).


-----Output-----

Print a single integer — the largest possible sum of squares that can be achieved after several (possibly zero) operations.


-----Examples-----
Input
1
123

Output
15129

Input
3
1 3 5

Output
51

Input
2
349525 699050

Output
1099509530625



-----Note-----

In the first sample no operation can be made, thus the answer is $123^2$.

In the second sample we can obtain the collection $1, 1, 7$, and $1^2 + 1^2 + 7^2 = 51$.

If $x$ and $y$ are represented in binary with equal number of bits (possibly with leading zeros), then each bit of $x~\mathsf{AND}~y$ is set to $1$ if and only if both corresponding bits of $x$ and $y$ are set to $1$. Similarly, each bit of $x~\mathsf{OR}~y$ is set to $1$ if and only if at least one of the corresponding bits of $x$ and $y$ are set to $1$. For example, $x = 3$ and $y = 5$ are represented as $011_2$ and $101_2$ (highest bit first). Then, $x~\mathsf{AND}~y = 001_2 = 1$, and $x~\mathsf{OR}~y = 111_2 = 7$.
"""

def largest_sum_of_squares(n, arr):
    if n == 1:
        return arr[0] ** 2
    
    max1 = max(arr)
    a = len(bin(max1)) - 2
    lis = [0] * a
    
    for i in range(a):
        for j in range(n):
            if arr[j] >= 2 ** i:
                x = bin(arr[j])
                x = x[2:]
                if x[-i - 1] == '1':
                    lis[i] += 1
    
    num = []
    b = max(lis)
    
    for i in range(b):
        s = 0
        for j in range(a):
            if lis[j] > 0:
                s += 2 ** j
                lis[j] -= 1
        num.append(s)
    
    ans = 0
    c = len(num)
    
    for i in range(c):
        ans += num[i] ** 2
    
    return ans