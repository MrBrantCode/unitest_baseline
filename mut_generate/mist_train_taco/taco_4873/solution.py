"""
QUESTION:
Jeff has become friends with Furik. Now these two are going to play one quite amusing game.

At the beginning of the game Jeff takes a piece of paper and writes down a permutation consisting of n numbers: p1, p2, ..., pn. Then the guys take turns to make moves, Jeff moves first. During his move, Jeff chooses two adjacent permutation elements and then the boy swaps them. During his move, Furic tosses a coin and if the coin shows "heads" he chooses a random pair of adjacent elements with indexes i and i + 1, for which an inequality pi > pi + 1 holds, and swaps them. But if the coin shows "tails", Furik chooses a random pair of adjacent elements with indexes i and i + 1, for which the inequality pi < pi + 1 holds, and swaps them. If the coin shows "heads" or "tails" and Furik has multiple ways of adjacent pairs to take, then he uniformly takes one of the pairs. If Furik doesn't have any pair to take, he tosses a coin one more time. The game ends when the permutation is sorted in the increasing order.

Jeff wants the game to finish as quickly as possible (that is, he wants both players to make as few moves as possible). Help Jeff find the minimum mathematical expectation of the number of moves in the game if he moves optimally well.

You can consider that the coin shows the heads (or tails) with the probability of 50 percent.

Input

The first line contains integer n (1 ≤ n ≤ 3000). The next line contains n distinct integers p1, p2, ..., pn (1 ≤ pi ≤ n) — the permutation p. The numbers are separated by spaces.

Output

In a single line print a single real value — the answer to the problem. The answer will be considered correct if the absolute or relative error doesn't exceed 10 - 6.

Examples

Input

2
1 2


Output

0.000000


Input

5
3 5 2 4 1


Output

13.000000

Note

In the first test the sequence is already sorted, so the answer is 0.
"""

def calculate_min_moves(n, permutation):
    def mergesort(l):
        l = list(l)
        if len(l) <= 1:
            return (l, 0)
        (left, linv) = mergesort(l[:len(l) // 2])
        (right, rinv) = mergesort(l[len(l) // 2:])
        lefti = 0
        righti = 0
        i = 0
        numinversions = 0
        while True:
            if i >= len(l):
                break
            if lefti >= len(left):
                l[i] = right[righti]
                righti += 1
            elif righti >= len(right):
                l[i] = left[lefti]
                lefti += 1
                numinversions += len(right)
            elif left[lefti] > right[righti]:
                l[i] = right[righti]
                righti += 1
            else:
                l[i] = left[lefti]
                lefti += 1
                numinversions += righti
            i += 1
        return (l, numinversions + linv + rinv)
    
    res = mergesort(permutation)
    num_inversions = res[1]
    
    if num_inversions % 2 == 0:
        return 2 * num_inversions
    else:
        return 2 * num_inversions - 1