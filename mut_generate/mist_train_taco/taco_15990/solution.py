"""
QUESTION:
Chef has two integers X and S. He is interested in sequences of non-negative integers such that the sum of their elements is S and the [bitwise OR] of their elements is X. Chef would like to know the shortest possible length such a sequence can have.

Formally, find the smallest positive integer N such that there exists a sequence A = [A_{1}, A_{2}, \ldots, A_{N}] satisfying the following conditions:
Each A_{i} is a non-negative integer
A_{1} + A_{2} + \ldots + A_{N} = S
A_{1} \vee A_{2} \vee \ldots \vee A_{N} = X

where \vee denotes the bitwise OR operation.

If there does not exist any sequence which satisfies the above conditions, output -1. Otherwise, output the minimum possible length of such a sequence.

------ Input Format ------ 

- The first line of input contains a single integer T, denoting the number of test cases. The description of T test cases follows.
- Each test case consists of a single line of input, containing two space-separated integers X and S — the required bitwise OR and sum, respectively.

------ Output Format ------ 

For each test case, output a single line containing one integer — the shortest possible length of such a sequence, or -1 if no such sequence exists.

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤ X ≤ S ≤ 10^{9}$

------ subtasks ------ 

Subtask #1 (100 points): Original constraints

----- Sample Input 1 ------ 
3
13 23
6 13
1 25

----- Sample Output 1 ------ 
3
-1
25

----- explanation 1 ------ 
Test Case $1$: One of the valid arrays of length $3$ is $[9,9,5]$. It can be shown that there is no valid array with length $< 3$.

Test Case $2$: There does not exist any sequence whose sum is $13$ and bitwise OR is $6$.

Test Case $3$: The valid array of minimum length contains $25$ ones.
"""

def binarize(num):
    powers = []
    power = 0
    while num > 0:
        bit = num % 2
        num = num // 2
        if bit:
            powers.append(power)
        power += 1
    return list(reversed(powers))

def possible(binx, s, mpw):
    for power in binx:
        val = 2 ** power
        times = min(s // val, mpw)
        s = s - val * times
    return s == 0

def optimize(binx, s, mn, mx):
    mid = (mn + mx) // 2
    if mid == mn:
        return mx
    if possible(binx, s, mid):
        return optimize(binx, s, mn, mid)
    else:
        return optimize(binx, s, mid, mx)

def find_shortest_sequence_length(x, s):
    if s < x:
        return -1
    origs = s
    repeats = 1
    s = s - x
    origs = s
    binx = binarize(x)
    mintimes = 0
    for power in binx:
        val = 2 ** power
        times = s // val
        s = s % val
        mintimes = max(mintimes, times)
    if s != 0:
        return -1
    return optimize(binx, origs, -1, mintimes) + repeats