"""
QUESTION:
There are N cats. We number them from 1 through N.

Each of the cats wears a hat. Cat i says: "there are exactly a_i different colors among the N - 1 hats worn by the cats except me."

Determine whether there exists a sequence of colors of the hats that is consistent with the remarks of the cats.

Constraints

* 2 ≤ N ≤ 10^5
* 1 ≤ a_i ≤ N-1

Input

Input is given from Standard Input in the following format:


N
a_1 a_2 ... a_N


Output

Print `Yes` if there exists a sequence of colors of the hats that is consistent with the remarks of the cats; print `No` otherwise.

Examples

Input

3
1 2 2


Output

Yes


Input

3
1 1 2


Output

No


Input

5
4 3 4 3 4


Output

No


Input

3
2 2 2


Output

Yes


Input

4
2 2 2 2


Output

Yes


Input

5
3 3 3 3 3


Output

No
"""

def is_hat_sequence_consistent(N, a):
    a.sort()
    min_val = a[0]
    max_val = a[N - 1]
    
    if max_val - min_val > 1:
        return 'No'
    elif max_val == min_val:
        if max_val <= N // 2 or max_val == N - 1:
            return 'Yes'
        else:
            return 'No'
    else:
        count_min = 0
        count_max = N
        for i in range(N):
            if a[i] < max_val:
                count_min += 1
                count_max -= 1
            else:
                break
        if count_min < max_val <= count_min + count_max // 2:
            return 'Yes'
        else:
            return 'No'