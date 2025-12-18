"""
QUESTION:
You are given a permutation P of length N.

You can perform the following operation on P:
Select two distinct indices i and j (1≤ i, j ≤ N) and swap the elements P_{i} and P_{j}.
The cost of the operation is abs(i-j).

The total cost is defined as the sum of costs of all operations performed.
Find the minimum total cost to sort the permutation in increasing order and the order of operations required to do so.

Note:
A permutation consists of all elements from 1 to N exactly once.
You do not need to minimise the number of operations required to sort the array. The number of operations can lie in the range [0, N^{2}].

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of multiple lines of input.
- The first line of each test case contains an integer N — the length of the permutation.
- The next line contains N space-separated integers, the elements of permutation P.

------ Output Format ------ 

For each test case:
- In the first line, output minimum total cost to sort the permutation in increasing order.
- In the next line, output an integer K (0≤ K ≤ N^{2}), denoting the number of operations required to sort the permutation.
- The next K lines contain two space-separated integers i and j, denoting the operation.

If there are multiple ways to sort the permutation using minimum total cost, print any.

------ Constraints ------ 

$1 ≤ T ≤ 100$
$2 ≤ N ≤ 500$
$P$ is a permutation of length $N$.
- The sum of $N$ over all test cases won't exceed $500$.

----- Sample Input 1 ------ 
3
3
1 3 2
4
1 2 3 4
4
2 1 4 3

----- Sample Output 1 ------ 
1
1
2 3
0
0
2
2
1 2
3 4

----- explanation 1 ------ 
Test case $1$: The minimum total cost to sort the permutation is $1$. We can sort the permutation using $1$ operation:
- Operation $1$: Choose $i = 2$ and $j = 3$ and swap $P_{2}$ and $P_{3}$. The cost of this operation is $abs(2-3) = 1$. The updated permutation is $[1, 2, 3]$, which is sorted.

Test case $2$: The permutation is already sorted. Thus, we require $0$ cost and $0$ operations to sort the permutation.

Test case $3$: The minimum total cost to sort the permutation is $2$. We can sort the permutation using $2$ operation:
- Operation $1$: Choose $i = 1$ and $j = 2$ and swap $P_{1}$ and $P_{1}$. The cost of this operation is $abs(1-2) = 1$. The updated permutation is $[1, 2, 4, 3]$.
- Operation $2$: Choose $i = 3$ and $j = 4$ and swap $P_{3}$ and $P_{4}$. The cost of this operation is $abs(3-4) = 1$. The updated permutation is $[1, 2, 3, 4]$, which is sorted.
"""

def minimum_cost_to_sort_permutation(N, P):
    def swap_with_next_negative(arr, ind, curswaps=[]):
        x = arr[ind]
        for i in range(ind, len(arr)):
            if arr[i] < 0:
                y = arr[i]
                arr[i] = x - (i - ind)
                arr[ind] = y + (i - ind)
                curswaps.append([ind + 1, i + 1])
                if arr[i] > 0:
                    (arr, curswaps) = swap_with_next_negative(arr, i, curswaps)
                return (arr, curswaps)
        return (arr, curswaps)

    D = [P[i - 1] - i for i in range(1, N + 1)]
    sum_ = sum([X for X in D if X > 0])
    swaps = []
    for z in range(N - 1, -1, -1):
        if D[z] > 0:
            (D, swaps_) = swap_with_next_negative(D, z, [])
            swaps += swaps_
    
    return sum_, swaps