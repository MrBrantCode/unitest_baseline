"""
QUESTION:
Chef has two arrays A and B of the same size N.

In one operation, Chef can:
Choose two integers i and j (1 ≤ i, j ≤ N) and swap the elements A_{i} and B_{j}.

Chef came up with a task to find the minimum possible value of (A_{max} - A_{min}) after performing the swap operation any (possibly zero) number of times. 

Since Chef is busy, can you help him solve this task?

Note that A_{max} and A_{min} denote the maximum and minimum elements of the array A respectively.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains one integer N — the number of elements in each array.
- The second line consists of N space-separated integers A_{1}, A_{2},\ldots ,A_{N} denoting the elements of the array A.
- The third line consists of N space-separated integers B_{1}, B_{2}, \ldots ,B_{N} denoting the elements of the array B.

------ Output Format ------ 

For each test case, output on a new line, the minimum possible value of (A_{max} - A_{min}) in the array A after doing swap operation any number of times.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 2\cdot 10^{5}$
$1 ≤ A_{i}, B_{i} ≤ 10^{9}$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^{5}$.

----- Sample Input 1 ------ 
3
3
2 1 3
1 4 1
4
2 1 4 3
3 2 6 2
5
2 8 4 9 7
7 3 6 8 4

----- Sample Output 1 ------ 
0
1
2
----- explanation 1 ------ 
Test case $1$: Chef can make the following operations:
- Operation $1$: Choose $i=1$ and $j=1$ and swap $A_{1}$ with $B_{1}$.
- Operation $2$: Choose $i=3$ and $j = 3$ and swap $A_{3}$ with $B_{3}$.

By doing the above operations, array $A$ becomes $[1, 1, 1]$. Here $(A_{max} - A_{min}) = 0$. It can be shown that this is the minimum value possible.

Test case $2$: Chef can make the following operations:
- Operation $1$: Choose $i=2$ and $j=2$ and swap $A_{2}$ with $B_{2}$.
- Operation $2$: Choose $i=3$ and $j=1$ and swap $A_{3}$ with $B_{1}$.
- Operation $3$: Choose $i=4$ and $j=4$ and swap $A_{4}$ with $B_{4}$.

By doing the above operations, array $A$ becomes $[2, 2, 3, 2]$. Here $(A_{max} - A_{min}) = 1$. It can be shown that this is the minimum value possible.

Test case $3$: Chef can make the following operations:
- Operation $1$: Choose $i=1$ and $j=1$ and swap $A_{1}$ with $B_{1}$.
- Operation $2$: Choose $i=3$ and $j=4$ and swap $A_{3}$ with $B_{4}$.

By doing the above operations, array $A$ becomes $[7, 8, 8, 9, 7]$. Here $(A_{max} - A_{min}) = 2$. It can be shown that this is the minimum value possible.
"""

def min_possible_value_after_swaps(T, test_cases):
    results = []
    for case in test_cases:
        N, A, B = case
        combined = A + B
        combined.sort()
        min_diff = float('inf')
        for i in range(N + 1):
            min_diff = min(min_diff, combined[i + N - 1] - combined[i])
        results.append(min_diff)
    return results