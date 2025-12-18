"""
QUESTION:
Author note: I think some of you might remember the problem "Two Melodies" from Eductational Codeforces Round 22. Now it's time to make it a bit more difficult!

Alice is a composer, and recently she had recorded two tracks that became very popular. Now she has got a lot of fans who are waiting for new tracks. 

This time Alice wants to form four melodies for her tracks.

Alice has a sheet with n notes written on it. She wants to take four such non-empty non-intersecting subsequences that all of them form a melody and sum of their lengths is maximal.

Subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

Subsequence forms a melody when each two adjacent notes either differ by 1 or are congruent modulo 7.

You should write a program which will calculate maximum sum of lengths of such four non-empty non-intersecting subsequences that all of them form a melody.

Input

The first line contains one integer number n (4 ≤ n ≤ 3000).

The second line contains n integer numbers a1, a2, ..., an (1 ≤ ai ≤ 105) — notes written on a sheet.

Output

Print maximum sum of lengths of such four non-empty non-intersecting subsequences that all of them form a melody.

Examples

Input

5
1 3 5 7 9


Output

4


Input

5
1 3 5 7 2


Output

5

Note

In the first example it is possible to compose 4 melodies by choosing any 4 notes (and each melody will consist of only one note).

In the second example it is possible to compose one melody with 2 notes — {1, 2}. Remaining notes are used in other three melodies (one note per each melody).
"""

def max_melody_lengths(n, notes):
    # Initialize the DP table
    dp = [[0] * (n + 1) for i in range(n + 1)]
    ans = 0
    
    # Initialize auxiliary arrays
    maxnum = [0] * (10 ** 5 + 2)
    maxmod = [0] * 7
    
    # Prepend a zero to the notes list for easier indexing
    notes = [0] + notes
    
    for y in range(n + 1):
        maxmod = [0] * 7
        for ai in notes:
            maxnum[ai] = 0
        for i in range(y):
            maxmod[notes[i] % 7] = max(maxmod[notes[i] % 7], dp[i][y])
            maxnum[notes[i]] = max(maxnum[notes[i]], dp[i][y])
        for x in range(y + 1, n + 1):
            dp[x][y] = max(maxmod[notes[x] % 7], maxnum[notes[x] + 1], maxnum[notes[x] - 1], dp[0][y]) + 1
            dp[y][x] = dp[x][y]
            maxmod[notes[x] % 7] = max(maxmod[notes[x] % 7], dp[x][y])
            maxnum[notes[x]] = max(maxnum[notes[x]], dp[x][y])
            ans = max(ans, dp[x][y])
    
    return ans