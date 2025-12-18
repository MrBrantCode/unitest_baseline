"""
QUESTION:
You've got a positive integer sequence a_1, a_2, ..., a_{n}. All numbers in the sequence are distinct. Let's fix the set of variables b_1, b_2, ..., b_{m}. Initially each variable b_{i} (1 ≤ i ≤ m) contains the value of zero. Consider the following sequence, consisting of n operations.

The first operation is assigning the value of a_1 to some variable b_{x} (1 ≤ x ≤ m). Each of the following n - 1 operations is assigning to some variable b_{y} the value that is equal to the sum of values that are stored in the variables b_{i} and b_{j} (1 ≤ i, j, y ≤ m). At that, the value that is assigned on the t-th operation, must equal a_{t}. For each operation numbers y, i, j are chosen anew.

Your task is to find the minimum number of variables m, such that those variables can help you perform the described sequence of operations.


-----Input-----

The first line contains integer n (1 ≤ n ≤ 23). The second line contains n space-separated integers a_1, a_2, ..., a_{n} (1 ≤ a_{k} ≤ 10^9).

It is guaranteed that all numbers in the sequence are distinct.


-----Output-----

In a single line print a single number — the minimum number of variables m, such that those variables can help you perform the described sequence of operations.

If you cannot perform the sequence of operations at any m, print -1.


-----Examples-----
Input
5
1 2 3 6 8

Output
2

Input
3
3 6 5

Output
-1

Input
6
2 4 8 6 10 18

Output
3



-----Note-----

In the first sample, you can use two variables b_1 and b_2 to perform the following sequence of operations.  b_1 := 1;  b_2 := b_1 + b_1;  b_1 := b_1 + b_2;  b_1 := b_1 + b_1;  b_1 := b_1 + b_2.
"""

def minimum_variables_needed(sequence):
    def can_solve(x, B):
        if (X, x, B) in memo:
            return memo[X, x, B]
        if len(B) > X:
            return False
        if x == len(sequence):
            return True
        if can_form(sequence[x], B):
            A = list(B)
            for e in range(len(B)):
                r = A[e]
                A[e] = sequence[x]
                if can_solve(x + 1, tuple(sorted(A))):
                    memo[X, x, B] = True
                    return True
                A[e] = r
            A.append(sequence[x])
            if can_solve(x + 1, tuple(sorted(A))):
                memo[X, x, B] = True
                return True
        memo[X, x, B] = False
        return False

    def can_form(x, B):
        for i in range(len(B)):
            for j in range(i, len(B)):
                if B[i] + B[j] == x:
                    return True
        return False

    n = len(sequence)
    memo = {}
    for X in range(1, n + 1):
        if can_solve(1, (sequence[0],)):
            return X
    return -1