"""
QUESTION:
Gru has a string $S$ of length $N$, consisting of only characters $a$ and $b$ for banana and $P$ points to spend.
Now Gru wants to replace and/or re-arrange characters of this given string to get the lexicographically smallest string possible. For this, he can perform the following two operations any number of times.
1) Swap any two characters in the string. This operation costs $1$ $point$. (any two, need not be adjacent)
2) Replace a character in the string with any other lower case english letter. This operation costs $2$ $points$.
Help Gru in obtaining the lexicographically smallest string possible, by using at most $P$ points.

-----Input:-----
- First line will contain $T$, number of testcases. Then the testcases follow. 
- Each testcase contains two lines of input, first-line containing two integers $N$ , $P$.
- The second line contains a string $S$ consisting of $N$ characters.

-----Output:-----
For each testcase, output in a single containing the lexicographically smallest string obtained.

-----Constraints-----
- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $0 \leq P \leq 2N$
- $S$ only consists of $'a'$ and $'b'$

-----Sample Input:-----
1
3 3
bba

-----Sample Output:-----
aab

-----Explanation:-----
We swap $S[0]$ and $S[2]$, to get $abb$. With the 2 remaining points, we replace $S[1]$ to obtain $aab$ which is the lexicographically smallest string possible for this case.
"""

def get_lexicographically_smallest_string(S: str, N: int, P: int) -> str:
    s = list(S)
    a = s.count('a')
    b = s.count('b')
    swap = 0
    arr = [i for i in s]
    
    for i in range(a):
        if s[i] == 'b':
            swap += 1
    
    if P <= swap:
        i = 0
        tmp = P
        while P > 0 and i < N:
            if arr[i] == 'b':
                arr[i] = 'a'
                P -= 1
            i += 1
        P = tmp
        i = N - 1
        while P > 0 and i > 0:
            if arr[i] == 'a':
                arr[i] = 'b'
                P -= 1
            i -= 1
        return ''.join(arr)
    else:
        for j in range(N):
            if j < a:
                arr[j] = 'a'
            else:
                arr[j] = 'b'
        P -= swap
        for k in range(N):
            if arr[k] == 'b':
                if s[k] == 'b' and P >= 2:
                    P -= 2
                    arr[k] = 'a'
                if s[k] == 'a' and P >= 1:
                    P -= 1
                    arr[k] = 'a'
        return ''.join(arr)