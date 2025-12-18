"""
QUESTION:
We have a sequence of length N consisting of non-negative integers. Consider performing the following operation on this sequence until the largest element in this sequence becomes N-1 or smaller. (The operation is the same as the one in Problem D.)

* Determine the largest element in the sequence (if there is more than one, choose one). Decrease the value of this element by N, and increase each of the other elements by 1.



It can be proved that the largest element in the sequence becomes N-1 or smaller after a finite number of operations.

You are given the sequence a_i. Find the number of times we will perform the above operation.

Constraints

* 2 ≤ N ≤ 50
* 0 ≤ a_i ≤ 10^{16} + 1000

Input

Input is given from Standard Input in the following format:


N
a_1 a_2 ... a_N


Output

Print the number of times the operation will be performed.

Examples

Input

4
3 3 3 3


Output

0


Input

3
1 0 3


Output

1


Input

2
2 2


Output

2


Input

7
27 0 0 0 0 0 0


Output

3


Input

10
1000 193 256 777 0 1 1192 1234567891011 48 425


Output

1234567894848
"""

def calculate_operations_count(N, A):
    A.sort(reverse=True)
    count = 0
    B = [A[0]]
    
    for i in range(N - 1):
        a = A[i + 1] + count
        C = []
        for b in B:
            x = (b - a) // (N + 1)
            C.append(x)
        s = sum(C)
        count += s
        new_B = []
        for (i, b) in enumerate(B):
            new_B.append(b + s - (N + 1) * C[i])
        new_B.append(a + s)
        B = new_B
    
    delta = max(min(B) - N, 0)
    count += delta * N
    for i in range(N):
        B[i] -= delta
    
    while max(B) > N - 1:
        tmp = -1
        for i in range(N):
            if B[i] > tmp:
                tmp = B[i]
                ind = i
        for i in range(N):
            if i == ind:
                B[i] -= N
            else:
                B[i] += 1
        count += 1
    
    return count