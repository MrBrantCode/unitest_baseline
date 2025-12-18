"""
QUESTION:
Tim buy a string of  length N from his friend which consist of  ‘d’ and ‘u’ letters only
,but now Tim wants to sell the string at maximum cost.  
The maximum cost of string is defined as the maximum length of a Substring (consecutive subsequence) consisting of equal letters.
Tim can change at most P characters of string (‘d’ to ‘u’   and   ‘u’ to ‘d’) you have to find out the maximum cost of string?

-----Input:-----
- First line will contain $N$ and $P$ .
- Second line will contain the String $S$.

-----Output:-----
Maximum cost of string S.

-----Constraints-----
- $1 \leq N\leq 10^5$
- $0 \leq P \leq N$

-----Sample Input 1:-----
4  2
$duud$

-----Sample Output 1:-----
4

-----Sample Input 2 :-----
10 1
$dduddudddu$

-----Sample Output 2:-----
6

-----EXPLANATION:-----
In the first sample input , We can obtain both strings $dddd$ and $uuuu$ .
In the second sample, the optimal answer is obtained with the string $dddddudd$ or with the string $dduddddd$
"""

def max_cost_of_string(N, P, S):
    d_count = S.count('d')
    u_count = S.count('u')
    
    if d_count <= P or u_count <= P:
        return N
    
    if d_count >= u_count:
        c = 0
        l = 0
        i = 0
        ii = -1
        pp = P
        while i < N:
            if S[i] == 'u' and ii == -1:
                ii = i
            if pp == 0 and S[i] == 'u':
                c = max(c, l)
                i = ii
                ii = -1
                l = -1
                pp = P
            elif S[i] == 'u':
                pp -= 1
            i += 1
            l += 1
        return max(c, l)
    else:
        c = 0
        l = 0
        i = 0
        ii = -1
        pp = P
        while i < N:
            if S[i] == 'd' and ii == -1:
                ii = i
            if pp == 0 and S[i] == 'd':
                c = max(c, l)
                i = ii
                ii = -1
                l = -1
                pp = P
            elif S[i] == 'd':
                pp -= 1
            i += 1
            l += 1
        return max(c, l)