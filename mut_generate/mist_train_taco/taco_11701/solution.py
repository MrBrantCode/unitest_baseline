"""
QUESTION:
<!--

Problem D

-->

Tally Counters

A number of tally counters are placed in a row. Pushing the button on a counter will increment the displayed value by one, or, when the value is already the maximum, it goes down to one. All the counters are of the same model with the same maximum value.

<image> Fig. D-1 Tally Counters

Starting from the values initially displayed on each of the counters, you want to change all the displayed values to target values specified for each. As you don't want the hassle, however, of pushing buttons of many counters one be one, you devised a special tool. Using the tool, you can push buttons of one or more adjacent counters, one push for each, in a single operation. You can choose an arbitrary number of counters at any position in each operation, as far as they are consecutively lined up.

How many operations are required at least to change the displayed values on counters to the target values?

Input

The input consists of multiple datasets, each in the following format.

> n m
>  a1 a2 ... an
>  b1 b2 ... bn
>

Each dataset consists of 3 lines. The first line contains n (1 ≤ n ≤ 1000) and m (1 ≤ m ≤ 10000), the number of counters and the maximum value displayed on counters, respectively. The second line contains the initial values on counters, ai (1 ≤ ai ≤ m), separated by spaces. The third line contains the target values on counters, bi (1 ≤ bi ≤ m), separated by spaces.

The end of the input is indicated by a line containing two zeros. The number of datasets does not exceed 100.

Output

For each dataset, print in a line the minimum number of operations required to make all of the counters display the target values.

Sample Input


4 5
2 3 1 4
2 5 5 2
3 100
1 10 100
1 10 100
5 10000
4971 7482 1238 8523 1823
3287 9013 9812 297 1809
0 0


Output for the Sample Input


4
0
14731






Example

Input

4 5
2 3 1 4
2 5 5 2
3 100
1 10 100
1 10 100
5 10000
4971 7482 1238 8523 1823
3287 9013 9812 297 1809
0 0


Output

4
0
14731
"""

def minimum_operations_to_target(n, m, initial_values, target_values):
    def solve(C, N, M, range=range, min=min):
        K = N // 4 + 1
        S = [0] * K
        T = [0] * K
        U = [0] * (K + 1)
        for i in range(N - 1):
            U[0] = 10 ** 18
            for j in range(K):
                U[j + 1] = min(U[j], S[j])
            k = K - 1
            ci = C[i]
            cj = C[i + 1]
            r = 10 ** 18
            for j in range(K - 1, -1, -1):
                while ci + k * M > cj + j * M:
                    r = min(r, ci + k * M + S[k])
                    k -= 1
                T[j] = min(r - j * M - cj, U[k + 1])
            (S, T) = (T, S)
        ci = C[-1]
        for i in range(K):
            S[i] += ci + i * M
        return min(S)

    C = [(b - a) % m for (a, b) in zip(initial_values, target_values)]
    return solve(C, n, m)