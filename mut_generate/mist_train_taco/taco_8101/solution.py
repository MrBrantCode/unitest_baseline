"""
QUESTION:
Polycarp loves geometric progressions very much. Since he was only three years old, he loves only the progressions of length three. He also has a favorite integer k and a sequence a, consisting of n integers.

He wants to know how many subsequences of length three can be selected from a, so that they form a geometric progression with common ratio k.

A subsequence of length three is a combination of three such indexes i_1, i_2, i_3, that 1 ≤ i_1 < i_2 < i_3 ≤ n. That is, a subsequence of length three are such groups of three elements that are not necessarily consecutive in the sequence, but their indexes are strictly increasing.

A geometric progression with common ratio k is a sequence of numbers of the form b·k^0, b·k^1, ..., b·k^{r} - 1.

Polycarp is only three years old, so he can not calculate this number himself. Help him to do it.


-----Input-----

The first line of the input contains two integers, n and k (1 ≤ n, k ≤ 2·10^5), showing how many numbers Polycarp's sequence has and his favorite number.

The second line contains n integers a_1, a_2, ..., a_{n} ( - 10^9 ≤ a_{i} ≤ 10^9) — elements of the sequence.


-----Output-----

Output a single number — the number of ways to choose a subsequence of length three, such that it forms a geometric progression with a common ratio k.


-----Examples-----
Input
5 2
1 1 2 2 4

Output
4
Input
3 1
1 1 1

Output
1
Input
10 3
1 2 6 2 3 6 9 18 3 9

Output
6


-----Note-----

In the first sample test the answer is four, as any of the two 1s can be chosen as the first element, the second element can be any of the 2s, and the third element of the subsequence must be equal to 4.
"""

def count_geometric_triplets(n: int, k: int, a: list) -> int:
    pos = {}
    ans = 0
    
    if k == 1:
        d = Counter(a)
        for i in d:
            if d[i] >= 3:
                t = d[i]
                ans += t * (t - 1) * (t - 2) // 6
    else:
        for i in range(n):
            if a[i] in pos:
                pos[a[i]].append(i)
            else:
                pos[a[i]] = [i]
        
        for i in range(1, n - 1):
            if a[i] % k == 0:
                x = a[i] // k
                y = a[i] * k
                if x in pos and y in pos:
                    px = bisect.bisect_left(pos[x], i - 1)
                    py = bisect.bisect_left(pos[y], i + 1)
                    if px != len(pos[x]):
                        if pos[x][px] > i - 1:
                            px -= 1
                        px += 1
                    ans += px * (len(pos[y]) - py)
    
    return ans