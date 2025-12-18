"""
QUESTION:
You are given an array $a$ consisting of $n$ integers. You can perform the following operations with it:   Choose some positions $i$ and $j$ ($1 \le i, j \le n, i \ne j$), write the value of $a_i \cdot a_j$ into the $j$-th cell and remove the number from the $i$-th cell;  Choose some position $i$ and remove the number from the $i$-th cell (this operation can be performed no more than once and at any point of time, not necessarily in the beginning). 

The number of elements decreases by one after each operation. However, the indexing of positions stays the same. Deleted numbers can't be used in the later operations.

Your task is to perform exactly $n - 1$ operations with the array in such a way that the only number that remains in the array is maximum possible. This number can be rather large, so instead of printing it you need to print any sequence of operations which leads to this maximum number. Read the output format to understand what exactly you need to print.


-----Input-----

The first line contains a single integer $n$ ($2 \le n \le 2 \cdot 10^5$) — the number of elements in the array.

The second line contains $n$ integers $a_1, a_2, \dots, a_n$ ($-10^9 \le a_i \le 10^9$) — the elements of the array.


-----Output-----

Print $n - 1$ lines. The $k$-th line should contain one of the two possible operations.

The operation of the first type should look like this: $1~ i_k~ j_k$, where $1$ is the type of operation, $i_k$ and $j_k$ are the positions of the chosen elements.

The operation of the second type should look like this: $2~ i_k$, where $2$ is the type of operation, $i_k$ is the position of the chosen element. Note that there should be no more than one such operation.

If there are multiple possible sequences of operations leading to the maximum number — print any of them.


-----Examples-----
Input
5
5 -2 0 1 -3

Output
2 3
1 1 2
1 2 4
1 4 5

Input
5
5 2 0 4 0

Output
1 3 5
2 5
1 1 2
1 2 4

Input
2
2 -1

Output
2 2

Input
4
0 -10 0 0

Output
1 1 2
1 2 3
1 3 4

Input
4
0 0 0 0

Output
1 1 2
1 2 3
1 3 4



-----Note-----

Let X be the removed number in the array. Let's take a look at all the examples:

The first example has, for example, the following sequence of transformations of the array: $[5, -2, 0, 1, -3] \to [5, -2, X, 1, -3] \to [X, -10, X, 1, -3] \to$ $[X, X, X, -10, -3] \to [X, X, X, X, 30]$. Thus, the maximum answer is $30$. Note, that other sequences that lead to the answer $30$ are also correct.

The second example has, for example, the following sequence of transformations of the array: $[5, 2, 0, 4, 0] \to [5, 2, X, 4, 0] \to [5, 2, X, 4, X] \to [X, 10, X, 4, X] \to$ $[X, X, X, 40, X]$. The following answer is also allowed: 

1 5 3

1 4 2

1 2 1

2 3



Then the sequence of transformations of the array will look like this: $[5, 2, 0, 4, 0] \to [5, 2, 0, 4, X] \to [5, 8, 0, X, X] \to [40, X, 0, X, X] \to$ $[40, X, X, X, X]$.

The third example can have the following sequence of transformations of the array: $[2, -1] \to [2, X]$.

The fourth example can have the following sequence of transformations of the array: $[0, -10, 0, 0] \to [X, 0, 0, 0] \to [X, X, 0, 0] \to [X, X, X, 0]$.

The fifth example can have the following sequence of transformations of the array: $[0, 0, 0, 0] \to [X, 0, 0, 0] \to [X, X, 0, 0] \to [X, X, X, 0]$.
"""

def maximize_remaining_number(n, num):
    visited = [True] * n
    negative = 0
    mn = -10 ** 10
    pos = -1
    zero = 0
    pos_zero = []
    
    # Identify zeros, negative numbers, and the most negative number
    for i in range(n):
        q = num[i]
        if q == 0:
            zero += 1
            pos_zero.append(i)
        elif q < 0:
            negative += 1
            if pos == -1:
                pos = i
            if mn < q:
                mn = q
                pos = i
    
    operations = []
    
    # Merge all zeros together
    for i in range(len(pos_zero) - 1):
        operations.append(f"1 {pos_zero[i] + 1} {pos_zero[i + 1] + 1}")
        visited[pos_zero[i]] = False
    
    t = n - zero
    
    # If there are zeros and an odd number of negatives, merge the most negative with the last zero
    if zero > 0 and negative % 2 == 1 and t > 0:
        operations.append(f"1 {pos + 1} {pos_zero[-1] + 1}")
        t -= 1
        visited[pos] = False
    
    # If there's an odd number of negatives and no zeros, remove the most negative number
    if negative % 2 == 1 and zero == 0 and t > 0:
        visited[pos] = False
        operations.append(f"2 {pos + 1}")
    # If there are zeros and more than one element left, remove the last zero
    elif zero > 0 and t > 0 and zero < n:
        visited[pos_zero[-1]] = False
        operations.append(f"2 {pos_zero[-1] + 1}")
    
    # Merge the remaining numbers
    old = None
    for i in range(n):
        if visited[i]:
            if old is None:
                old = i
            else:
                operations.append(f"1 {old + 1} {i + 1}")
                old = i
    
    return operations