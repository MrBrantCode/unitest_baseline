"""
QUESTION:
Read problem statements in [Hindi], [Bengali], [Mandarin Chinese], [Russian], and [Vietnamese] as well.

Chef's apartment consists of $M$ floors (numbered $1$ through $M$), and there's an elevator that is used to move between different floors. The elevator is connected with a computer which registers its movement in a sequence $B$. Whenever the elevator moves to a different floor, the computer appends the new floor number to sequence $B$. Currently, the sequence $B$ has $N$ elements.

Unfortunately, the computer is infected with a virus which replaced some elements of $B$ by $-1$s. Chef now wants to know what could be the minimum number of times the elevator has changed its direction. That is, how many times the elevator was going up then started going down and vice versa. 

Help chef by answering his question or determine that the sequence $B$ is invalid.

------ Input: ------

The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two integers $N$ and $M$. 
The second line contains $N$ space-separated integers $B_{1}, B_{2}, \ldots, B_{N}$.

------ Output: ------
For each test case, print a single line containing one integer ― the minimum number of times the elevator has changed its direction or $-1$ if the given $B$ sequence is invalid.

------ Constraints  ------
$1 ≤ T ≤ 1000$
$1 ≤ N ≤ 10^{5}$
$2 ≤ M ≤ 10^{5}$
$1 ≤ B_{i} ≤ M$ or $B_{i} = -1$ for each valid $i$
sum of $N$ over all test-cases doesn't exceed $10^{6}$

------  Subtasks ------
Subtask #1 (50 points):
$N ≤ 1,000$
the sum of $N$ over all test cases does not exceed $10,000$

Subtask #2 (50 points): Original constraints

------ Sample Input: ------

5
4 5
2 3 4 3
4 5
2 -1 4 3
4 5
1 -1 -1 5
5 4
-1 -1 3 -1 -1
5 5
-1 -1 3 -1 -1

------ Sample Output: ------

1
1
-1
1
0
"""

def calculate_min_direction_changes(N, M, B):
    ans = float('inf')
    for pp in range(2):
        lpoz = -1
        sw = 0
        prev = B[0]
        dir = True
        if prev == -1:
            prev = 1
        else:
            lpoz = 0
        for i in range(1, N):
            if B[i] != -1:
                j = lpoz
                if j != -1:
                    if (i - j) % 2 != abs(B[i] - B[j]) % 2 or abs(B[i] - B[j]) > abs(i - j):
                        ans = -1
                        break
                lpoz = i
            if dir and prev == M:
                sw += 1
                dir = not dir
            elif not dir and prev == 1:
                sw += 1
                dir = not dir
            if dir:
                prev = prev + 1
            else:
                prev = prev - 1
            if B[i] != -1 and not (dir and prev <= B[i] or (not dir and prev >= B[i])):
                sw += 1
                dir = not dir
            if B[i] != -1:
                prev = B[i]
        if ans != -1 and ans > sw:
            ans = sw
        for i in range(N):
            if 1 <= B[i] <= M:
                B[i] = M + 1 - B[i]
    return ans if ans != float('inf') else -1