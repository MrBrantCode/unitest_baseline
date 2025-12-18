"""
QUESTION:
Read problems statements in [Mandarin Chinese], [Russian], [Vietnamese] and [Bengali] as well.

A permutation is an array consisting of $N$ distinct integers from $1$ to $N$ in arbitrary order.

Chef has two permutation arrays $A$ and $P$ of length $N$. Chef performs the following three types of operations on the array $A$:
$1$ : Permute the array $A$ according to the order defined by permutation $P$.That is, replace $A$ with the array $B$ where $B[P[i]]=A[i]$.
$2 \ x \ y$ : Swap the elements at positions $x$ and $y$ in $A$.
$3 \ x$ : Output the element at position $x$ in array $A$. 

For each operation of type $3$, Chef wants you to output the element at position $x$ in array $A$ after all preceding operations have been applied.

------ Input ------

The first line contains an integer $T$, the number of test cases. Then the test cases follow. 
The first line of each test case contains a single integer $N$.
The second line contains $N$ integers denoting elements of array $A$.
The third line contains $N$ integers denoting elements of array $P$.
The fourth line contains a single integer $Q$, denoting the number of operations to be performed.
$Q$ lines follow, each describing an operation of one of the three types above.

------ Output ------
For each test case, for each query of type $3$, output the answer in a separate line.

------ Constraints ------
$1 ≤ T ≤ 1000$
$1 ≤ N, Q ≤ 10^{5}$
$1 ≤ A[i],P[i], x, y ≤ N$
$A$ and $P$ are permutations.
$x\ne y$ in type $2$ operations.
The sum of $N$ and the sum of $Q$ over all test cases do not exceed $10^{5}$.

----- Sample Input 1 ------ 
1

3

1 2 3

2 3 1

3

1

2 2 3

3 1
----- Sample Output 1 ------ 
3
----- explanation 1 ------ 
Initially, array $A$ is $[1,2,3]$.
It changes as follows: $[1,2,3]$ -> $[3,1,2]$ -> $[3,2,1]$.
So, we output element at position $1$ in array $A$, which is $3$.
"""

def process_permutations(T, test_cases):
    results = []
    
    for test_case in test_cases:
        n = test_case['N']
        a = test_case['A']
        p = test_case['P']
        q = test_case['Q']
        operations = test_case['operations']
        
        cycles = []
        cycle = [0] * n
        index_in_cycle = [0] * n
        determine_cycles(p, n, cycles)
        no_of_cycles = len(cycles)
        
        for i in range(no_of_cycles):
            cycle_i = cycles[i]
            for j in range(len(cycle_i)):
                c = cycles[i][j]
                cycle[c - 1] = i
                index_in_cycle[c - 1] = j
        
        no_of_permutations = 0
        test_results = []
        
        for query in operations:
            if query[0] == 1:
                no_of_permutations += 1
            elif query[0] == 2:
                x = query[1] - 1
                y = query[2] - 1
                x1 = get_value(no_of_permutations, x, cycles, cycle, index_in_cycle)
                y1 = get_value(no_of_permutations, y, cycles, cycle, index_in_cycle)
                (a[x1], a[y1]) = (a[y1], a[x1])
            else:
                ind = query[1] - 1
                test_results.append(a[get_value(no_of_permutations, ind, cycles, cycle, index_in_cycle)])
        
        results.append(test_results)
    
    return results

def get_value(k, ind, cycles, cycle, index_in_cycle):
    m = len(cycles[cycle[ind]])
    return cycles[cycle[ind]][index_in_cycle[ind] - k % m] - 1

def determine_cycles(p, n, cycles):
    visited = [False] * n
    i = 1
    while i <= n:
        if not visited[i - 1]:
            visited[i - 1] = True
            cycles.append([i])
            j = p[i - 1]
            while j != i:
                visited[j - 1] = True
                cycles[-1].append(j)
                j = p[j - 1]
        i = i + 1