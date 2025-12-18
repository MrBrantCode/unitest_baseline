"""
QUESTION:
There is a sequence X of length N, where every element is initially 0. Let X_i denote the i-th element of X.

You are given a sequence A of length N. The i-th element of A is A_i. Determine if we can make X equal to A by repeating the operation below. If we can, find the minimum number of operations required.

* Choose an integer i such that 1\leq i\leq N-1. Replace the value of X_{i+1} with the value of X_i plus 1.

Constraints

* 1 \leq N \leq 2 \times 10^5
* 0 \leq A_i \leq 10^9(1\leq i\leq N)
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
A_1
:
A_N


Output

If we can make X equal to A by repeating the operation, print the minimum number of operations required. If we cannot, print -1.

Examples

Input

4
0
1
1
2


Output

3


Input

3
1
2
1


Output

-1


Input

9
0
1
1
0
1
2
2
1
2


Output

8
"""

def min_operations_to_transform(N, A):
    # Check if the first element of A is not 0, which is impossible to achieve
    if A[0] != 0:
        return -1
    
    ans = 0
    
    for i in range(1, N):
        if A[i] - A[i - 1] >= 2:
            return -1
        elif A[i] > A[i - 1]:
            ans += 1
        else:
            ans += A[i]
    
    return ans