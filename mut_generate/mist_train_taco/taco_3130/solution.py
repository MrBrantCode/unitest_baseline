"""
QUESTION:
Eugene loves sequences, especially arithmetic progressions. One day he was asked to solve a difficult problem.

If a sequence of numbers A1, A2, ... , AN form an arithmetic progression A, he was asked to calculate sum of F(Ai), for L ≤ i ≤ R.
F(X) is defined as:

If X < 10 then F(X) = X.

Else F(X) = F(sum_of_digits(X)).

Example:
F(1378) = 
F(1+3+7+8) = 
F(19) = 
F(1 + 9) = 
F(10) = 
F(1+0) = 
F(1) = 1

-----Input-----
- The first line of the input contains an integer T denoting the number of test cases.
- Each test case is described in one line containing four integers: A1 denoting the first element of the arithmetic progression A, D denoting the common difference between successive members of A, and L and R as described in the problem statement.

-----Output-----
- For each test case, output a single line containing one integer denoting sum of F(Ai).

-----Constraints-----
- 1 ≤ T ≤ 105
- 1 ≤ A1 ≤ 109
- 0 ≤ D ≤ 109
- 1 ≤ R ≤ 1018
- 1 ≤ L ≤ R

-----Subtasks-----
- Subtask 1:  0 ≤ D ≤ 100, 1 ≤ A1 ≤ 109, 1 ≤ R ≤ 100  - 15 points
- Subtask 2:  0 ≤ D ≤ 109, 1 ≤ A1 ≤ 109, 1 ≤ R ≤ 106  - 25 points
- Subtask 3: Original constraints - 60 points

-----Example-----
Input:
2
1 1 1 3
14 7 2 4

Output:
6
12

-----Explanation-----
Example case 1.
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...}
A1 = 1
A2 = 2
A3 = 3
F(A1) = 1
F(A2) = 2
F(A3) = 3
1+2+3=6
Example case 2.
A = {14, 21, 28, 35, 42, 49, 56, 63, 70, 77,  ...}
A2 = 21
A3 = 28
A4 = 35
F(A2) = 3
F(A3) = 1
F(A4) = 8
3+1+8=12
"""

def calculate_sum_of_F(A1, D, L, R):
    def sum_func(x):
        if x < 10:
            return x
        if x in sum_cache:
            return sum_cache[x]
        xx = sum(int(digit) for digit in str(x))
        result = sum_func(xx)
        sum_cache[x] = result
        return result

    sum_cache = {}
    cycle_table = [
        [9, [1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [9, [1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [3, [1, 0, 0, 1, 0, 0, 1, 0, 0]],
        [9, [1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [9, [1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [3, [1, 0, 0, 1, 0, 0, 1, 0, 0]],
        [9, [1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [9, [1, 1, 1, 1, 1, 1, 1, 1, 1]],
        [1, [1, 0, 0, 0, 0, 0, 0, 0, 0]]
    ]
    NUMBER = 9

    A_L = A1 + D * (L - 1)
    A_L_kfunc = sum_func(A_L)
    D_kfunc = sum_func(D)
    n = R - L + 1

    if D == 0:
        return n * A_L_kfunc

    cycle_len = cycle_table[D_kfunc - 1][0]
    cycle_markers = cycle_table[D_kfunc - 1][1]
    whole_part = n // cycle_len
    remainder = n % cycle_len

    counts = [whole_part * x for x in cycle_markers]
    pos = 0
    for i in range(remainder):
        counts[pos] += 1
        pos = (pos + D_kfunc) % NUMBER

    result = 0
    for i, x in enumerate(counts):
        value = (A_L_kfunc - 1 + i) % NUMBER + 1
        result += value * x

    return result