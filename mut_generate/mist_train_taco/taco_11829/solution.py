"""
QUESTION:
You are given an array [A_{1}, \ldots, A_{N}]. You want to split it into several (≥ 2) [subarrays] so that the following condition holds:

Calculate the sum of elements in each subarray. Then, the AND of all these sums is nonzero, where AND denotes the bitwise AND operation.

Determine if it's possible. If it's possible, find one such split. You don't have to minimize the number of subarrays.

------ Input Format ------ 

- The first line of the input contains a single integer T - the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer N - the length of the array.
- The second line of each test case contains N space-separated integers A_{1}, A_{2}, \ldots, A_{N}.

------ Output Format ------ 

For each test case, if it's not possible to split the array so that the condition from the statement holds, output NO. 

Otherwise, output YES. In the next line, output K (2 ≤ K ≤ N) - the number of subarrays you are splitting into. 

In the i-th of the next K lines, output two integers L_{i}, R_{i} (1 ≤ L_{i} ≤ R_{i} ≤ N), where [L_{i}, R_{i}] denotes the i-th subarray. 

Each number from 1 to N has to appear in exactly one of the segments [L_{i}, R_{i}].

You can output each letter in either uppercase or lowercase. You can output any solution. You don't have to minimize K.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$2 ≤ N ≤ 10^{5}$
$0 ≤ A_{i} < 2^{30}$
- Sum of $N$ over all test cases doesn't exceed $2\cdot 10^{5}$

----- Sample Input 1 ------ 
5
4
1 9 8 4
3
0 0 0
2
16 15
5
1 2 6 24 120
7
8 6 0 16 24 0 8

----- Sample Output 1 ------ 
YES
2
2 4
1 1
NO
NO
YES
2
1 2
3 5
YES
3
1 1
6 7
2 5
----- explanation 1 ------ 
Test case $1$: You can split the array into two subarrays $[2, 4]$ and $[1, 1]$. They have sums $21$ and $1$ correspondingly, whose AND is $1$.

Test case $4$: You can split the array into two subarrays $[1, 2]$ and $[3, 5]$. They have sums $3$ and $150$ correspondingly, whose AND is $2$.

Test case $5$: You can split the array into three subarrays $[1, 1]$, $[6, 7]$, $[2, 5]$. They have sums $8$, $8$, $46$, whose AND is $8$.

It's possible to show that it's impossible to split in the desired way in the second and the third test cases.
"""

def can_split_array_with_nonzero_and(test_cases):
    results = []
    
    for n, array in test_cases:
        f = 0
        b = [[0 for _ in range(31)] for _ in range(n)]
        
        for i in range(n):
            x = array[i]
            j = 0
            while x > 0:
                d = x % 2
                x //= 2
                b[i][j] = d
                j += 1
        
        bit = 0
        while bit < 31:
            a = []
            for i in range(n):
                if b[i][bit] == 1:
                    a.append(i + 1)
            bit += 1
            if len(a) < 2:
                continue
            
            f = 1
            subarrays = []
            subarrays.append((1, a[0]))
            a[-1] = n
            for i in range(len(a) - 1):
                subarrays.append((a[i] + 1, a[i + 1]))
            results.append((True, subarrays))
            break
        
        if f == 0:
            results.append((False, []))
    
    return results