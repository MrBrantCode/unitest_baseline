"""
QUESTION:
Mike has a sequence A = [a1, a2, ..., an] of length n. He considers the sequence B = [b1, b2, ..., bn] beautiful if the gcd of all its elements is bigger than 1, i.e. <image>. 

Mike wants to change his sequence in order to make it beautiful. In one move he can choose an index i (1 ≤ i < n), delete numbers ai, ai + 1 and put numbers ai - ai + 1, ai + ai + 1 in their place instead, in this order. He wants perform as few operations as possible. Find the minimal number of operations to make sequence A beautiful if it's possible, or tell him that it is impossible to do so.

<image> is the biggest non-negative number d such that d divides bi for every i (1 ≤ i ≤ n).

Input

The first line contains a single integer n (2 ≤ n ≤ 100 000) — length of sequence A.

The second line contains n space-separated integers a1, a2, ..., an (1 ≤ ai ≤ 109) — elements of sequence A.

Output

Output on the first line "YES" (without quotes) if it is possible to make sequence A beautiful by performing operations described above, and "NO" (without quotes) otherwise.

If the answer was "YES", output the minimal number of moves needed to make sequence A beautiful.

Examples

Input

2
1 1


Output

YES
1


Input

3
6 2 4


Output

YES
0


Input

2
1 3


Output

YES
1

Note

In the first example you can simply make one move to obtain sequence [0, 2] with <image>.

In the second example the gcd of the sequence is already greater than 1.
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def make_sequence_beautiful(n, a):
    g = a[0]
    for i in range(n):
        g = gcd(a[i], g)
    
    if g > 1:
        return "YES", 0
    
    ans = 0
    l = 0
    
    for i in range(n):
        if a[i] % 2:
            l += 1
        else:
            if l % 2:
                ans += l // 2 + 2
            else:
                ans += l // 2
            l = 0
    
    if l % 2:
        ans += l // 2 + 2
    else:
        ans += l // 2
    
    return "YES", ans