"""
QUESTION:
Omy and Ish were learning the pattern printing. In order to learn they give themselves a task. In this task they are given a string and they have to form a pyramid with the pattern as follows:
RowNumber are one based indexed.
- 
If (RowNumber % 3 == 0) then string is written in left to right while in other cases it is written in right to left order.
- 
if the string end it will be started again and end of the pyramid need not to be the end of string.
For eg: string is “$CODING$” and height of pyramid is “$5$”
C
D O
I N G
I D O C
D O C G N

Omi will be asked $Q$ queries and he has to tell the frequency of a character  C in that particular row $R$ of pyramid.

-----Input:-----
- First line will contain $N$, height of pyramid.
- Next line contain a string consists only of Uppercase English Alphabets, length not exceed $10^6$
- Third line contain a single integer $Q$, the number of queries to be asked.
- Each query contain two space separated integers, $R$ and $C$, where $R$ is the row number and $C$ is the character.

-----Output:-----
- For each query, output in a single line the frequency of the alphabet in the given row.

-----Constraints:-----
- $1$ $\leq$ $N$ $\leq$ $10$^$18$
- $1$ $\leq$ $Q$ $\leq$ $50000$
- $1 \leq R \leq N$
- $A \leq C \leq Z$

-----Sample Input:-----
5
CODING
2
1 C
2 D

-----Sample Output:-----
1
1
"""

def calculate_character_frequency_in_pyramid(n, s, queries):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    arr = [0] * 26
    pref = []
    
    # Build the prefix sum array
    for i in range(len(s)):
        for j in range(26):
            if alph[j] == s[i]:
                arr[j] += 1
                break
        pref.append(arr[:])
    
    results = []
    
    for (r, c) in queries:
        r = int(r)
        ind = alph.index(c)
        
        prev = ((r - 1) ** 2 + r - 1) // 2
        done = prev % len(s)
        ans = 0
        rem = (len(s) - done) % len(s)
        
        if r <= rem:
            if done > 0:
                results.append(pref[done + r - 1][ind] - pref[done - 1][ind])
            else:
                results.append(pref[done + r - 1][ind])
            continue
        
        if rem != 0:
            if done > 0:
                ans += pref[-1][ind] - pref[done - 1][ind]
            else:
                ans += pref[-1][ind]
            r -= rem
        
        ans += pref[-1][ind] * (r // len(s))
        r %= len(s)
        
        if r != 0:
            ans += pref[r - 1][ind]
        
        results.append(ans)
    
    return results