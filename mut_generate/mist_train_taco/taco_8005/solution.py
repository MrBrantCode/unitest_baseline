"""
QUESTION:
There are N boxes arranged in a circle. The i-th box contains A_i stones.

Determine whether it is possible to remove all the stones from the boxes by repeatedly performing the following operation:

* Select one box. Let the box be the i-th box. Then, for each j from 1 through N, remove exactly j stones from the (i+j)-th box. Here, the (N+k)-th box is identified with the k-th box.



Note that the operation cannot be performed if there is a box that does not contain enough number of stones to be removed.

Constraints

* 1 ≦ N ≦ 10^5
* 1 ≦ A_i ≦ 10^9

Input

The input is given from Standard Input in the following format:


N
A_1 A_2 … A_N


Output

If it is possible to remove all the stones from the boxes, print `YES`. Otherwise, print `NO`.

Examples

Input

5
4 5 1 2 3


Output

YES


Input

5
6 9 12 10 8


Output

YES


Input

4
1 2 3 1


Output

NO
"""

def can_remove_all_stones(N, A):
    s = sum(A)
    K = s // (N * (N + 1) // 2)
    
    if N == 1:
        return 'YES'
    
    if s % (N * (N + 1) // 2) != 0:
        return 'NO'
    
    d = [0] * (N - 1)
    for i in range(N - 1):
        d[i] = A[i + 1] - A[i] - K
    
    for i in range(N - 1):
        if d[i] > 0 or abs(d[i]) % N != 0:
            return 'NO'
    
    return 'YES'