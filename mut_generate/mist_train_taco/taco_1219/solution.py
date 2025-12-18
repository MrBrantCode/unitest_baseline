"""
QUESTION:
Consider a string of $n$ characters, $\boldsymbol{\mathrm{~S~}}$, of where each character is indexed from $\mbox{0}$ to $n-1$.

You are given $\textit{q}$ queries in the form of two integer indices: ${\mbox{left}}$ and $\textit{right}$. For each query, count and print the number of different substrings of $\boldsymbol{\mathrm{~S~}}$ in the inclusive range between ${\mbox{left}}$ and $\textit{right}$. 

Note: Two substrings are different if their sequence of characters differs by at least one. For example, given the string $\boldsymbol{s}=$ aab, substrings $\boldsymbol{s}_{[0,0]}=$ a and $\boldsymbol{s}_{[1,1]}\:=\:$ a are the same but substrings $\textbf{s}_{[0,1]}\:=\:$ aa and $\boldsymbol{s}_{[1,2]}=$ ab are different.

Input Format

The first line contains two space-separated integers describing the respective values of $n$ and $\textit{q}$. 

The second line contains a single string denoting $\boldsymbol{\mathrm{~S~}}$. 

Each of the $\textit{q}$ subsequent lines contains two space-separated integers describing the respective values of ${\mbox{left}}$ and $\textit{right}$ for a query.

Constraints

$0\leq left\leq right\leq n-1$  
String $\boldsymbol{\mathrm{~S~}}$ consists of lowercase English alphabetic letters (i.e., a to z) only.

Subtasks  

For $30\%$ of the test cases, $1\leq n,q\leq100$  
For $50\%$ of the test cases, $1\leq n,q\leq3000$  
For $100\%$ of the test cases, $1\leq n,q\leq10^5$  

Output Format

For each query, print the number of different substrings in the inclusive range between index ${\mbox{left}}$ and index $\textit{right}$ on a new line. 

Sample Input 0
5 5
aabaa
1 1
1 4
1 1
1 4
0 2

Sample Output 0
1
8
1
8
5

Explanation 0

Given $\boldsymbol{s}=$ aabaa, we perform the following $q=5$ queries:

1 1: The only substring of a is itself, so we print $\mbox{1}$ on a new line.
1 4: The substrings of abaa are a, b, ab, ba, aa, aba, baa, and abaa, so we print $8$ on a new line.
1 1: The only substring of a is itself, so we print $\mbox{1}$ on a new line.
1 4: The substrings of abaa are a, b, ab, ba, aa, aba, baa, and abaa, so we print $8$ on a new line.
0 2: The substrings of aab are a, b, aa, ab, and aab, so we print $5$ on a new line.
"""

def count_distinct_substrings(s, left, right):
    def kasai(s, suff, n):
        lcp = [0] * n
        inv = [0] * n
        for i in range(n):
            inv[suff[i]] = i
        k = 0
        for i in range(n):
            if inv[i] == n - 1:
                k = 0
                continue
            j = suff[inv[i] + 1]
            while i + k < n and j + k < n and (s[i + k] == s[j + k]):
                k += 1
            lcp[inv[i]] = k
            if k > 0:
                k -= 1
        return lcp
    
    sub = s[left:right + 1]
    length = right - left + 1
    suffix = [[i, sub[i:]] for i in range(length)]
    suffix.sort(key=lambda x: x[1])
    suff, suffix = [list(t) for t in zip(*suffix)]
    lcp = kasai(sub, suff, length)
    
    count = len(suffix[0])
    for i in range(length - 1):
        count += len(suffix[i + 1]) - lcp[i]
    
    return count