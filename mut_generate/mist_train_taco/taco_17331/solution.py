"""
QUESTION:
Pavel cooks barbecue. There are n skewers, they lay on a brazier in a row, each on one of n positions. Pavel wants each skewer to be cooked some time in every of n positions in two directions: in the one it was directed originally and in the reversed direction.

Pavel has a plan: a permutation p and a sequence b1, b2, ..., bn, consisting of zeros and ones. Each second Pavel move skewer on position i to position pi, and if bi equals 1 then he reverses it. So he hope that every skewer will visit every position in both directions.

Unfortunately, not every pair of permutation p and sequence b suits Pavel. What is the minimum total number of elements in the given permutation p and the given sequence b he needs to change so that every skewer will visit each of 2n placements? Note that after changing the permutation should remain a permutation as well.

There is no problem for Pavel, if some skewer visits some of the placements several times before he ends to cook. In other words, a permutation p and a sequence b suit him if there is an integer k (k ≥ 2n), so that after k seconds each skewer visits each of the 2n placements.

It can be shown that some suitable pair of permutation p and sequence b exists for any n.

Input

The first line contain the integer n (1 ≤ n ≤ 2·105) — the number of skewers.

The second line contains a sequence of integers p1, p2, ..., pn (1 ≤ pi ≤ n) — the permutation, according to which Pavel wants to move the skewers.

The third line contains a sequence b1, b2, ..., bn consisting of zeros and ones, according to which Pavel wants to reverse the skewers.

Output

Print single integer — the minimum total number of elements in the given permutation p and the given sequence b he needs to change so that every skewer will visit each of 2n placements.

Examples

Input

4
4 3 2 1
0 1 1 1


Output

2


Input

3
2 3 1
0 0 0


Output

1

Note

In the first example Pavel can change the permutation to 4, 3, 1, 2.

In the second example Pavel can change any element of b to 1.
"""

def min_changes_for_skewers(n, p, b):
    # Calculate the sum of the sequence b
    s = sum(b)
    
    # Determine if we need to change any element in b
    if s % 2 == 0:
        ans = 1
    else:
        ans = 0
    
    # Initialize visited array to track visited positions
    visited = [0] * n
    ptr = 0
    start = 1
    visited[0] = 1
    q = 1
    c = 1
    
    # Traverse the permutation to count cycles
    while q < n:
        start = p[start - 1]
        if visited[start - 1] == 1:
            c += 1
            while ptr < n and visited[ptr] == 1:
                ptr += 1
            start = ptr + 1
        else:
            visited[start - 1] = 1
            q += 1
    
    # If there's only one cycle, return the current answer
    if c == 1:
        return ans
    else:
        return ans + c