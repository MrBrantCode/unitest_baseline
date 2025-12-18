"""
QUESTION:
Cherry has a string S$S$ consisting of lowercase English letters. Using this string, he formed a pyramid of infinite length with certain rules:
- N$N$-th row of pyramid contains N$N$ characters.
- Each row of pyramid begins with the first character of the string.
- The subsequent characters of the row are appended to the string in cyclic fashion, until the size of string for that Row is reached (See example pyramid for better understanding).
He has another string T$T$ of smaller (or equal) size.
You are asked Q$Q$ queries. Each query is provided with a row number N$N$. The answer to the query is number of occurrences of string T$T$ in that particular row of pyramid. No of occurrences of String T$T$ in a string V$V$ would mean that you'd need to find number of substrings Vi,Vi+1...Vj$V_i, V_{i+1} ... V_j$ which are equal to String T$T$, where i≤j$i \leq j$.
For eg: If the string is code, then the pyramid will be of the form:
c
co
cod
code
codec
codeco
codecod
codecode
codecodec
codecodeco
...

-----Input:-----
- The first line contains string S$S$ — consisting of lowercase English letters.
- The second line contains string T$T$ — consisting of lowercase English letters.
- Next line contains an integer Q$Q$ — the number of queries.
- Then follow Q$Q$ lines with queries descriptions. Each of them contains a single integer N$N$ denoting the row number of pyramid.

-----Output:-----
- Print Q$Q$ lines. The i$i$-th of them should contain a integer denoting occurrences of string T$T$ in that particular row.

-----Constraints-----
- 1≤|S|≤105$1 \leq |S| \leq 10^5$
- 1≤|T|≤|S|$1 \leq |T| \leq |S|$
- 1≤Q≤105$1 \leq Q \leq 10^5$
- 1≤N≤109$1 \leq N \leq 10^9$

-----Sample Input:-----
codechef
chefcode
3
4
12
1455

-----Sample Output:-----
0
1
181

-----Explanation:-----
Pyramid will be formed as explained in the statement.
Query 1: Row number 4 of the pyramid is code. The number of occurrences of chefcode in code is 0.
Query 2: Row number 12 of the pyramid is codechefcode. The number of occurrences of chefcode in codechefcode is 1.
"""

def count_occurrences_in_pyramid_row(S, T, N):
    def kmp(s, t, lps):
        n = len(s)
        m = len(t)
        count = [0 for x in range(n)]
        i = 0
        j = 0
        while i < n:
            count[i] = count[i - 1]
            if t[j] == s[i]:
                i += 1
                j += 1
            if j == m:
                count[i - 1] += 1
                j = lps[j - 1]
            elif i < n and t[j] != s[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return count

    def lpsa(t, m):
        l = 0
        lps = [0 for i in range(m)]
        i = 1
        while i < m:
            if t[i] == t[l]:
                l += 1
                lps[i] = l
                i += 1
            elif l != 0:
                l = lps[l - 1]
            else:
                lps[i] = 0
                i += 1
        return lps

    n = len(S)
    m = len(T)
    lps = lpsa(T, m)
    one = kmp(S, T, lps)[-1]
    count = kmp(S + S, T, lps)
    two = count[-1]
    three = two - 2 * one

    v = N // n
    if v:
        ans = v * one + (v - 1) * three
        e = N % n
        ans += count[n - 1 + e] - count[n - 1]
    else:
        e = N % n
        ans = count[e - 1]

    return ans