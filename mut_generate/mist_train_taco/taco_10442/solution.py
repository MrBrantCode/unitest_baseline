"""
QUESTION:
Aoki loves numerical sequences and trees.

One day, Takahashi gave him an integer sequence of length N, a_1, a_2, ..., a_N, which made him want to construct a tree.

Aoki wants to construct a tree with N vertices numbered 1 through N, such that for each i = 1,2,...,N, the distance between vertex i and the farthest vertex from it is a_i, assuming that the length of each edge is 1.

Determine whether such a tree exists.

Constraints

* 2 ≦ N ≦ 100
* 1 ≦ a_i ≦ N-1

Input

The input is given from Standard Input in the following format:


N
a_1 a_2 ... a_N


Output

If there exists a tree that satisfies the condition, print `Possible`. Otherwise, print `Impossible`.

Examples

Input

5
3 2 2 3 3


Output

Possible


Input

3
1 1 2


Output

Impossible


Input

10
1 2 2 2 2 2 2 2 2 2


Output

Possible


Input

10
1 1 2 2 2 2 2 2 2 2


Output

Impossible


Input

6
1 1 1 1 1 5


Output

Impossible


Input

5
4 3 2 3 4


Output

Possible
"""

from collections import defaultdict

def is_tree_possible(N, a):
    D = defaultdict(int)
    a = sorted(a)
    
    if N == 2:
        if a[0] != 1 or a[1] != 1:
            return 'Impossible'
        else:
            return 'Possible'
    else:
        for i in range(N):
            D[a[i]] += 1
        
        if a[-1] % 2 != 0:
            if a[0] * 2 - 1 != a[-1]:
                return 'Impossible'
            else:
                judge = 'Possible'
                if D[a[0]] != 2:
                    judge = 'Impossible'
                for i in range(a[0], a[-1] + 1):
                    if D[i] < 2:
                        judge = 'Impossible'
                        break
                return judge
        else:
            judge = 'Possible'
            if a[0] * 2 != a[-1]:
                return 'Impossible'
            else:
                judge = 'Possible'
                if D[a[0]] != 1:
                    judge = 'Impossible'
                for i in range(a[0] + 1, a[-1] + 1):
                    if D[i] < 2:
                        judge = 'Impossible'
                        break
                return judge