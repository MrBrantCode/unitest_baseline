"""
QUESTION:
You are given a permutation P_1 ... P_N of the set {1, 2, ..., N}.

You can apply the following operation to this permutation, any number of times (possibly zero):

* Choose two indices i,j (1 ≦ i < j ≦ N), such that j - i ≧ K and |P_i - P_j| = 1. Then, swap the values of P_i and P_j.



Among all permutations that can be obtained by applying this operation to the given permutation, find the lexicographically smallest one.

Constraints

* 2≦N≦500,000
* 1≦K≦N-1
* P is a permutation of the set {1, 2, ..., N}.

Input

The input is given from Standard Input in the following format:


N K
P_1 P_2 ... P_N


Output

Print the lexicographically smallest permutation that can be obtained.

Examples

Input

4 2
4 2 3 1


Output

2
1
4
3


Input

5 1
5 4 3 2 1


Output

1
2
3
4
5


Input

8 3
4 5 7 8 3 1 2 6


Output

1
2
6
7
5
3
4
8
"""

def find_lexicographically_smallest_permutation(N, K, P):
    def invert(p, q):
        for (i, pi) in enumerate(p):
            q[pi] = i

    def sort_insertion(k, data, first, last):
        length = last - first
        if length <= 2:
            if length == 2 and data[first] - data[first + 1] >= k:
                (data[first], data[first + 1]) = (data[first + 1], data[first])
            return
        for i in range(first + 1, last):
            v = data[i]
            for t in range(i - 1, first - 1, -1):
                if data[t] - v < k:
                    t += 1
                    break
            data[t + 1:i + 1] = data[t:i]
            data[t] = v

    def sort_merge(k, data, first, last):
        if last - first < 10:
            sort_insertion(k, data, first, last)
            return
        middle = (first + last) // 2
        sort_merge(k, data, first, middle)
        sort_merge(k, data, middle, last)
        bounds = data[first:middle]
        for i in range(len(bounds) - 2, -1, -1):
            bounds[i] = min(bounds[i + 1], bounds[i])
        tmp = data[first:middle]
        first_len = middle - first
        head1 = 0
        head2 = middle
        for ohead in range(first, last):
            if head1 == first_len or head2 == last:
                data[ohead:ohead + first_len - head1] = tmp[head1:first_len]
                return
            elif bounds[head1] - data[head2] >= k:
                data[ohead] = data[head2]
                head2 += 1
            else:
                data[ohead] = tmp[head1]
                head1 += 1

    # Adjust P to be zero-indexed
    P = [p - 1 for p in P]
    q = list(P)
    invert(P, q)
    sort_merge(K, q, 0, N)
    invert(q, P)
    # Adjust P back to one-indexed
    return [p + 1 for p in P]