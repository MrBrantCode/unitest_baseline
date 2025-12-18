"""
QUESTION:
You are given a sequence of numbers a_1, a_2, ..., a_{n}, and a number m.

Check if it is possible to choose a non-empty subsequence a_{i}_{j} such that the sum of numbers in this subsequence is divisible by m.


-----Input-----

The first line contains two numbers, n and m (1 ≤ n ≤ 10^6, 2 ≤ m ≤ 10^3) — the size of the original sequence and the number such that sum should be divisible by it.

The second line contains n integers a_1, a_2, ..., a_{n} (0 ≤ a_{i} ≤ 10^9).


-----Output-----

In the single line print either "YES" (without the quotes) if there exists the sought subsequence, or "NO" (without the quotes), if such subsequence doesn't exist.


-----Examples-----
Input
3 5
1 2 3

Output
YES

Input
1 6
5

Output
NO

Input
4 6
3 1 1 3

Output
YES

Input
6 6
5 5 5 5 5 5

Output
YES



-----Note-----

In the first sample test you can choose numbers 2 and 3, the sum of which is divisible by 5.

In the second sample test the single non-empty subsequence of numbers is a single number 5. Number 5 is not divisible by 6, that is, the sought subsequence doesn't exist.

In the third sample test you need to choose two numbers 3 on the ends.

In the fourth sample test you can take the whole subsequence.
"""

def is_subsequence_sum_divisible(n, m, sequence):
    # Calculate the modulo of each number in the sequence
    modnums = [num % m for num in sequence]
    
    # Dictionary to count occurrences of each modulo result
    cnt = {}
    # Dictionary to store possible sums for each modulo result
    vars = {}
    
    for v in modnums:
        if v not in cnt:
            cnt[v] = 0
            vars[v] = set([])
        cnt[v] += 1
    
    # Check for each modulo result if we can form a sum divisible by m
    for v in vars.keys():
        cur = v
        for j in range(cnt[v]):
            if cur in vars[v]:
                break
            vars[v].add(cur)
            if cur == 0:
                return 'YES'
            cur = (cur + v) % m
    
    # Check combinations of modulo results
    cur = set([0])
    for var in vars.keys():
        for s in set(cur):
            for v in vars[var]:
                res = v + s
                if res == m:
                    return 'YES'
                cur.add(res % m)
    
    return 'NO'