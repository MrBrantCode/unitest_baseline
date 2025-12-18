"""
QUESTION:
Takahashi loves sorting.

He has a permutation (p_1,p_2,...,p_N) of the integers from 1 through N. Now, he will repeat the following operation until the permutation becomes (1,2,...,N):

* First, we will define high and low elements in the permutation, as follows. The i-th element in the permutation is high if the maximum element between the 1-st and i-th elements, inclusive, is the i-th element itself, and otherwise the i-th element is low.
* Then, let a_1,a_2,...,a_k be the values of the high elements, and b_1,b_2,...,b_{N-k} be the values of the low elements in the current permutation, in the order they appear in it.
* Lastly, rearrange the permutation into (b_1,b_2,...,b_{N-k},a_1,a_2,...,a_k).



How many operations are necessary until the permutation is sorted?

Constraints

* 1 ≤ N ≤ 2×10^5
* (p_1,p_2,...,p_N) is a permutation of the integers from 1 through N.

Input

Input is given from Standard Input in the following format:


N
p_1 p_2 ... p_N


Output

Print the number of operations that are necessary until the permutation is sorted.

Examples

Input

5
3 5 1 2 4


Output

3


Input

5
5 4 3 2 1


Output

4


Input

10
2 10 5 7 3 6 4 9 8 1


Output

6
"""

def count_sorting_operations(N, P):
    if N == 1:
        return 0
    
    Pi = [0] * (N + 1)
    for (i, n) in enumerate(P, 1):
        Pi[n] = i
    
    T = [0] * N
    f = [0] * N
    
    if Pi[N] > Pi[N - 1]:
        T[N - 1] = 0
        f[N - 1] = N - 1
    else:
        T[N - 1] = 1
        f[N - 1] = N
    
    for i in range(N - 2, 0, -1):
        if T[i + 1] == 0:
            i_i = Pi[i]
            i_ii = Pi[i + 1]
            if i_ii > i_i:
                T[i] = T[i + 1]
                f[i] = f[i + 1]
            else:
                T[i] = T[i + 1] + 1
                f[i] = i + 1
        else:
            i_f = Pi[f[i + 1]]
            i_i = Pi[i]
            i_ii = Pi[i + 1]
            if i_f < i_i < i_ii or i_ii < i_f < i_i or i_i < i_ii < i_f:
                T[i] = T[i + 1]
                f[i] = f[i + 1]
            else:
                T[i] = T[i + 1] + 1
                f[i] = i + 1
    
    return T[1]