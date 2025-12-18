"""
QUESTION:
Monocarp has got two strings $s$ and $t$ having equal length. Both strings consist of lowercase Latin letters "a" and "b". 

Monocarp wants to make these two strings $s$ and $t$ equal to each other. He can do the following operation any number of times: choose an index $pos_1$ in the string $s$, choose an index $pos_2$ in the string $t$, and swap $s_{pos_1}$ with $t_{pos_2}$.

You have to determine the minimum number of operations Monocarp has to perform to make $s$ and $t$ equal, and print any optimal sequence of operations — or say that it is impossible to make these strings equal.


-----Input-----

The first line contains one integer $n$ $(1 \le n \le 2 \cdot 10^{5})$ — the length of $s$ and $t$.

The second line contains one string $s$ consisting of $n$ characters "a" and "b". 

The third line contains one string $t$ consisting of $n$ characters "a" and "b". 


-----Output-----

If it is impossible to make these strings equal, print $-1$.

Otherwise, in the first line print $k$ — the minimum number of operations required to make the strings equal. In each of the next $k$ lines print two integers — the index in the string $s$ and the index in the string $t$ that should be used in the corresponding swap operation. 


-----Examples-----
Input
4
abab
aabb

Output
2
3 3
3 2

Input
1
a
b

Output
-1

Input
8
babbaabb
abababaa

Output
3
2 6
1 3
7 8



-----Note-----

In the first example two operations are enough. For example, you can swap the third letter in $s$ with the third letter in $t$. Then $s = $ "abbb", $t = $ "aaab". Then swap the third letter in $s$ and the second letter in $t$. Then both $s$ and $t$ are equal to "abab".

In the second example it's impossible to make two strings equal.
"""

def make_strings_equal(s: str, t: str) -> tuple:
    n = len(s)
    cnt = {}
    
    # Count occurrences of 'a' and 'b' in both strings
    for i in range(n):
        if s[i] not in cnt:
            cnt[s[i]] = 1
        else:
            cnt[s[i]] += 1
        if t[i] not in cnt:
            cnt[t[i]] = 1
        else:
            cnt[t[i]] += 1
    
    # Check if the total count of 'a' and 'b' is even
    for key in cnt:
        if cnt[key] % 2 != 0:
            return -1, []
    
    ans = []
    ff = deque([])
    ss = deque([])
    
    # Identify positions where characters differ
    for i in range(n):
        if s[i] == t[i]:
            continue
        if s[i] == 'a' and t[i] == 'b':
            ff.append(i + 1)
        else:
            ss.append(i + 1)
    
    # Perform swaps to make the strings equal
    while len(ff) > 1:
        t1 = ff.popleft()
        t2 = ff.popleft()
        ans.append((t2, t1))
    
    while len(ss) > 1:
        t1 = ss.popleft()
        t2 = ss.popleft()
        ans.append((t1, t2))
    
    if len(ff) > 0:
        t1 = ff.popleft()
        t2 = ss.popleft()
        ans.append((t2, t2))
        ans.append((t1, t2))
    
    return len(ans), ans