"""
QUESTION:
This challenge uses the famous KMP algorithm. It isn't really important to understand how KMP works, but you should understand what it calculates.

A KMP algorithm takes a string, $\mbox{S}$, of length $N$ as input. Let's assume that the characters in $\mbox{S}$ are indexed from $\mbox{1}$ to $N$; for every prefix of $\mbox{S}$, the algorithm calculates the length of its longest valid border in linear complexity. In other words, for every $\boldsymbol{i}$ (where $1\leq i\leq N$) it calculates the largest $\boldsymbol{l}$ (where $0\leq l\leq i-1$) such that for every $\boldsymbol{p}$ (where $1\leq p\leq l$) there is $S[p]=S[i-l+p]$.

Here is an implementation example of KMP:

kmp[1] = 0;
for (i = 2; i <= N; i = i + 1){
    l = kmp[i - 1];
    while (l > 0 && S[i] != S[l + 1]){
        l = kmp[l];
    }
    if (S[i] == S[l + 1]){
        kmp[i] = l + 1;
    }
    else{
        kmp[i] = 0;
    }
}

Given a sequence $x_1,x_2,\ldots,x_{26}$, construct a string, $\mbox{S}$, that meets the following conditions:

The frequency of letter '$\boldsymbol{a}$' in $\mbox{S}$ is exactly $x_1$, the frequency of letter '$\boldsymbol{b}$' in $\mbox{S}$ is exactly $x_2$, and so on.
Let's assume characters of $\mbox{S}$ are numbered from $\mbox{1}$ to $N$, where $\sum\limits_{i=1}^{n}x_{i}=N$. We apply the KMP algorithm to $\mbox{S}$ and get a table, $kmp$, of size $N$. You must ensure that the sum of $kmp[i]$ for all $\boldsymbol{i}$ is minimal.

If there are multiple strings which fulfill the above conditions, print the lexicographically smallest one.

Input Format

A single line containing $26$ space-separated integers describing sequence $\boldsymbol{x}$. 

Constraints

The sum of all $x_i$ will be a positive integer $\leq10^{6}$.

Output Format

Print a single string denoting $\mbox{S}$.

Sample Input
2 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

Sample Output
aabb

Explanation

The output string must have two '$\boldsymbol{a}$' and two '$\boldsymbol{b}$'. There are several such strings but we must ensure that sum of $kmp[i]$ for all $1<=i<=4$ is minimal. See the figure below:

The minimum sum is $\mbox{1}$. Among all the strings that satisfy both the condition, "aabb" is the lexicographically smallest.
"""

from string import ascii_lowercase as A

def construct_minimal_kmp_string(x):
    used = [i for i in range(26) if x[i]]
    if len(used) == 0:
        return ""
    if len(used) == 1:
        return A[used[0]] * x[used[0]]
    
    f = min(used, key=lambda a: (x[a], a))
    used = [a for a in used if a != f]
    
    if x[f] == 1:
        return A[f] + ''.join((A[c] * x[c] for c in used))
    elif f > used[0]:
        x[f] -= 1
        return A[f] + ''.join((A[c] * x[c] for c in range(26)))
    elif 2 * (x[f] - 2) <= sum(x) - 2:
        res = 2 * A[f]
        b = ''.join((A[c] * x[c] for c in used))
        x[f] -= 2
        i = 0
        while x[f]:
            res += b[i] + A[f]
            i += 1
            x[f] -= 1
        res += b[i:]
        return res
    else:
        x[f] -= 1
        x[used[0]] -= 1
        return A[f] + A[used[0]] + A[f] * x[f] + ''.join((A[c] * x[c] for c in used))