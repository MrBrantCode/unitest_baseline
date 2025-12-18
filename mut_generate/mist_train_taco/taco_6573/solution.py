"""
QUESTION:
There are N integers, A_1, A_2, ..., A_N, written on a blackboard.

We will repeat the following operation N-1 times so that we have only one integer on the blackboard.

* Choose two integers x and y on the blackboard and erase these two integers. Then, write a new integer x-y.



Find the maximum possible value of the final integer on the blackboard and a sequence of operations that maximizes the final integer.

Constraints

* 2 \leq N \leq 10^5
* -10^4 \leq A_i \leq 10^4
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N
A_1 A_2 ... A_N


Output

Print the maximum possible value M of the final integer on the blackboard, and a sequence of operations x_i, y_i that maximizes the final integer, in the format below.

Here x_i and y_i represent the integers x and y chosen in the i-th operation, respectively.

If there are multiple sequences of operations that maximize the final integer, any of them will be accepted.


M
x_1 y_1
:
x_{N-1} y_{N-1}

Output

Print the maximum possible value M of the final integer on the blackboard, and a sequence of operations x_i, y_i that maximizes the final integer, in the format below.

Here x_i and y_i represent the integers x and y chosen in the i-th operation, respectively.

If there are multiple sequences of operations that maximize the final integer, any of them will be accepted.


M
x_1 y_1
:
x_{N-1} y_{N-1}

Examples

Input

3
1 -1 2


Output

4
-1 1
2 -2


Input

3
1 1 1


Output

1
1 1
1 0
"""

def maximize_final_integer(N, A):
    A.sort()
    M = sum(abs(i) for i in A) - 2 * min(abs(A[-1]), abs(A[0])) * (A[0] * A[-1] > 0)
    operations = []
    
    if A[0] > 0:
        operations.append((A[0], A[-1]))
        A[0] -= A[-1]
        for i in A[1:-2]:
            operations.append((A[0], i))
            A[0] -= i
        operations.append((A[-2], A[0]))
    elif A[-1] < 0:
        for i in A[:-1]:
            operations.append((A[-1], i))
            A[-1] -= i
    else:
        for i in A[1:-1]:
            if i < 0:
                operations.append((A[-1], i))
                A[-1] -= i
            else:
                operations.append((A[0], i))
                A[0] -= i
        operations.append((A[-1], A[0]))
    
    return M, operations