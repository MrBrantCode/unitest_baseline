"""
QUESTION:
Polycarp loves geometric progressions — he collects them. However, as such progressions occur very rarely, he also loves the sequences of numbers where it is enough to delete a single element to get a geometric progression.

In this task we shall define geometric progressions as finite sequences of numbers a1, a2, ..., ak, where ai = c·bi - 1 for some real numbers c and b. For example, the sequences [2, -4, 8], [0, 0, 0, 0], [199] are geometric progressions and [0, 1, 2, 3] is not.

Recently Polycarp has found a sequence and he can't classify it. Help him to do it. Determine whether it is a geometric progression. If it is not, check if it can become a geometric progression if an element is deleted from it.

Input

The first line contains an integer n (1 ≤ n ≤ 105) — the number of elements in the given sequence. The second line contains the given sequence. The numbers are space-separated. All the elements of the given sequence are integers and their absolute value does not exceed 104.

Output

Print 0, if the given sequence is a geometric progression. Otherwise, check if it is possible to make the sequence a geometric progression by deleting a single element. If it is possible, print 1. If it is impossible, print 2.

Examples

Input

4
3 6 12 24


Output

0


Input

4
-8 -16 24 -32


Output

1


Input

4
0 1 2 3


Output

2
"""

def check_geometric_progression(sequence):
    n = len(sequence)
    
    if n == 1:
        return 0
    
    if n == 2:
        if sequence[0] == 0 and sequence[1] != 0:
            return 1
        return 0
    
    def div(a, b):
        if b == 0:
            return 0 if a == 0 else 'inf'
        return a / b
    
    (pref, suff) = ([['init', 1]], [['init', 1]])
    
    for i in range(1, n):
        d = div(sequence[i], sequence[i - 1])
        if pref[-1][0] == 'init':
            pass
        elif d != pref[-1][0]:
            for j in range(i, n):
                pref += [['null', 0]]
            break
        pref += [[d, 1]]
    
    for i in range(n - 1, -1, -1):
        d = div(sequence[i], sequence[i - 1])
        if sequence[i - 1] == 0 and sequence[i] != 0:
            suff[-1][0] = suff[-2][0] if len(suff) > 1 else 1
        if d != suff[-1][0] and suff[-1][0] != 'init':
            for j in range(i - 1, -1, -1):
                suff += [['null', 0]]
            break
        suff += [[d, 1]]
    
    if pref[-1][1] == 1:
        return 0
    
    if pref[-2][1] == 1 or suff[-2][1] == 1:
        return 1
    
    for i in range(1, n - 1):
        (pr, sf) = (pref[i - 1], suff[n - i - 2])
        dv = div(sequence[i + 1], sequence[i - 1])
        if pr[0] == 'init' and sf[0] == 'init':
            return 1
        if pr[0] == 'init' and dv == sf[0]:
            return 1
        elif sf[0] == 'init' and dv == pr[0]:
            return 1
        elif dv == pr[0] and dv == sf[0]:
            return 1
    
    return 2