"""
QUESTION:
The brave Knight came to the King and asked permission to marry the princess. The King knew that the Knight was brave, but he also wanted to know if he was smart enough. So he asked him to solve the following task.

There is a permutation $p_i$ of numbers from 1 to $2n$. You can make two types of operations.

Swap $p_1$ and $p_2$, $p_3$ and $p_4$, ..., $p_{2n-1}$ and $p_{2n}$.

Swap $p_1$ and $p_{n+1}$, $p_2$ and $p_{n+2}$, ..., $p_{n}$ and $p_{2n}$.

The task is to find the minimal number of operations required to sort the given permutation.

The Knight was not that smart actually, but quite charming, so the princess asks you to help him to solve the King's task.


-----Input-----

The first line contains the integer $n$ ($1\le n\le 1000$). The second line contains $2n$ integers $p_i$ — the permutation of numbers from 1 to $2n$.


-----Output-----

Print one integer — the minimal number of operations required to sort the permutation. If it is impossible to sort the permutation using these operations, print $-1$.


-----Examples-----

Input
3
6 3 2 5 4 1
Output
3
Input
2
3 4 2 1
Output
-1
Input
4
1 2 3 4 5 6 7 8
Output
0


-----Note-----

In the first example, you can sort the permutation in three operations:

Make operation 1: $3, 6, 5, 2, 1, 4$.

Make operation 2: $2, 1, 4, 3, 6, 5$.

Make operation 1: $1, 2, 3, 4, 5, 6$.
"""

def min_operations_to_sort_permutation(n, permutation):
    def swap1(arr):
        for i in range(0, len(arr) - 1, 2):
            (arr[i], arr[i + 1]) = (arr[i + 1], arr[i])
        return arr

    def swap2(arr):
        for i in range(0, len(arr) // 2):
            (arr[i], arr[i + len(arr) // 2]) = (arr[i + len(arr) // 2], arr[i])
        return arr

    target = list(range(1, 2 * n + 1))
    per = permutation[:]
    per1 = permutation[:]
    i = 0

    while per != target and per1 != target:
        if i > 2 * n:
            return -1
        if i % 2 == 0:
            per = swap1(per)
            per1 = swap2(per1)
        else:
            per = swap2(per)
            per1 = swap1(per1)
        i += 1

    return i