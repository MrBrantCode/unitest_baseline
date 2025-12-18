"""
QUESTION:
Chef has an array A of length N such that A_{i} = i.

In one operation, Chef can pick any two elements of the array, delete them from A, and append either their [bitwise XOR] or their [bitwise OR] to A.

Note that after each operation, the length of the array decreases by 1.

Let F be the final number obtained after N-1 operations are made. You are given an integer X, determine if you can get F=X via some sequence of operations.

In case it is possible to get F = X, print the operations too (see the section Output format for more details), otherwise print -1.

------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of a single line containing two space-separated integers N and X.

------ Output Format ------ 

For each test case, output -1 if it is impossible to get X in the end.
Otherwise print N-1 lines denoting the operations.

On each line, print
- 1\ x\ y if you want replace x and y with x\ OR\ y.
- 2\ x\ y if you want replace x and y with x\ XOR\ y.

Note that x and y are the elements of the array at the time of applying the operation, and if either of them is not present in the array you will receive a WA verdict.

------ Constraints ------ 

$1 ≤ T ≤ 5000$
$2 ≤ N ≤ 2^{15}$
$1 ≤ X ≤ 2^{16} - 1$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^{5}$.

----- Sample Input 1 ------ 
3
3 2
2 2
4 7

----- Sample Output 1 ------ 
2 1 3
1 2 2
-1
1 1 2
1 3 3
1 3 4

----- explanation 1 ------ 
Test case $1$: The operations are as follows:
- Initially, the array is $A = [1, 2, 3]$
- The first move removes $1$ and $3$ and appends their $XOR$, making the array $A = [2, 2]$
- The second move removes $2$ and $2$ and appends their $OR$, making the array $A = [2]$

Test case $2$: It can be shown that no sequence of operations can achieve $F = 2$ in this case.

Test case $3$: The operations are as follows:
- Initially, the array is $A = [1, 2, 3, 4]$
- After the first move, the array is $A = [3, 4, 3]$
- After the second move, the array is $A = [4, 3]$
- After the third move, the array is $A = [7]$
"""

def determine_operations(N, X):
    if N == 2 and X == 2:
        return -1
    if N == 2 and X == 3:
        return [(1, 1, 2)]
    
    nb = bin(N)[2:]
    xb = bin(X)[2:]
    
    if len(xb) > len(nb):
        return -1
    
    if len(nb) > len(xb):
        if nb[1:] == '0' * (len(nb) - 1):
            return -1
    
    st_pow = set()
    i = 1
    while i <= N:
        st_pow.add(i)
        i *= 2
    
    operations = []
    curr = 3
    for i in range(4, N + 1):
        if i not in st_pow:
            operations.append((1, curr, i))
            curr |= i
    
    xb = xb[::-1]
    for i in range(len(xb)):
        p = pow(2, i)
        if xb[i] == '0':
            operations.append((2, curr, p))
            st_pow.remove(p)
            curr ^= p
        else:
            operations.append((1, curr, p))
            st_pow.remove(p)
            curr |= p
    
    if len(st_pow) > 0:
        a = list(st_pow)
        for z in a:
            operations.append((2, curr, z))
            curr ^= z
    
    return operations