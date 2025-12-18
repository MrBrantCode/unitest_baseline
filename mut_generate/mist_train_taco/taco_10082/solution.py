"""
QUESTION:
Chef has two arrays A and B of the same size N.

In one operation, Chef can:
Choose an index i (1 ≤ i ≤ N) and swap the elements A_{i} and B_{i}.

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
2
1 2
2 1
3
1 5 3
2 3 1
4
4 2 5 1
5 3 4 1

----- Sample Output 1 ------ 
0
1
3

----- explanation 1 ------ 
Test case $1$: Chef can make the following operations:
- Operation $1$: Choose $i=1$ and swap $A_{1}$ with $B_{1}$.

By doing the above operations, array $A$ becomes $[2, 2]$. Here $(A_{max} - A_{min}) = 0$. It can be shown that this is the minimum value possible.

Test case $2$: Chef can make the following operations:
- Operation $1$: Choose $i=1$ and swap $A_{1}$ with $B_{1}$.
- Operation $2$: Choose $i=2$ and swap $A_{2}$ with $B_{2}$.

By doing the above operations, array $A$ becomes $[2, 3, 3]$. Here $(A_{max} - A_{min}) = 1$. It can be shown that this is the minimum value possible.

Test case $3$: Chef can make the following operations:
- Operation $1$: Choose $i=2$ and swap $A_{2}$ with $B_{2}$.
- Operation $2$: Choose $i=3$ and swap $A_{3}$ with $B_{3}$.

By doing the above operations, array $A$ becomes $[4, 3, 4, 1]$. Here $(A_{max} - A_{min}) = 3$. It can be shown that this is the minimum value possible.
"""

def min_possible_value_after_swaps(A, B):
    N = len(A)
    
    # Swap elements in A and B such that A[i] >= B[i] for all i
    for i in range(N):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
    
    # Create a combined array of pairs (A[i], B[i]) and sort it
    combined = [(A[i], B[i]) for i in range(N)]
    combined.sort()
    
    # Initialize min and max arrays for A and B
    arr1Min = [0] * N
    arr1Max = [0] * N
    arr2Min = [0] * N
    arr2Max = [0] * N
    
    # Fill the min and max arrays for A
    arr1Min[0] = combined[0][0]
    arr1Max[0] = combined[0][0]
    for i in range(1, N):
        arr1Min[i] = min(arr1Min[i - 1], combined[i][0])
        arr1Max[i] = max(arr1Max[i - 1], combined[i][0])
    
    # Fill the min and max arrays for B
    arr2Min[N - 1] = combined[N - 1][1]
    arr2Max[N - 1] = combined[N - 1][1]
    for i in range(N - 2, -1, -1):
        arr2Min[i] = min(arr2Min[i + 1], combined[i][1])
        arr2Max[i] = max(arr2Max[i + 1], combined[i][1])
    
    # Calculate the minimum possible value of (A_max - A_min)
    ans = combined[N - 1][0] - combined[0][0]
    for i in range(N - 1, -1, -1):
        if i == 0:
            maximum = arr2Max[0]
            minimum = arr2Min[0]
        else:
            maximum = max(arr1Max[i - 1], arr2Max[i])
            minimum = min(arr1Min[i - 1], arr2Min[i])
        ans = min(ans, maximum - minimum)
    
    return ans