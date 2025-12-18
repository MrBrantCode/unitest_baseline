"""
QUESTION:
Little Petya likes to play very much. And most of all he likes to play the following game:

He is given a sequence of N integer numbers. At each step it is allowed to increase the value of any number by 1 or to decrease it by 1. The goal of the game is to make the sequence non-decreasing with the smallest number of steps. Petya is not good at math, so he asks for your help.

The sequence a is called non-decreasing if a1 ≤ a2 ≤ ... ≤ aN holds, where N is the length of the sequence.

Input

The first line of the input contains single integer N (1 ≤ N ≤ 5000) — the length of the initial sequence. The following N lines contain one integer each — elements of the sequence. These numbers do not exceed 109 by absolute value.

Output

Output one integer — minimum number of steps required to achieve the goal.

Examples

Input

5
3 2 -1 2 11


Output

4


Input

5
2 1 1 1 1


Output

1
"""

from bisect import insort

def min_steps_to_non_decreasing(arr):
    pri_q = []
    ans = 0
    for n in arr:
        if pri_q:
            if pri_q[-1] > n:
                ans += pri_q[-1] - n
                pri_q.pop()
                insort(pri_q, n)
        insort(pri_q, n)
    return ans