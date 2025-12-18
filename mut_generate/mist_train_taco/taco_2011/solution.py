"""
QUESTION:
You are given an array ${A}$ of size $N$. You are asked to answer ${Q}$ queries. 

Each query is of the form : 

${ij x}$ 

You need to print Yes if ${x}$ divides the value returned from $find(i,j)$ function, otherwise print No.

find(int i,int j)
{
    if(i>j) return 1;
    ans = pow(A[i],find(i+1,j))
    return ans
}

Input Format

First line of the input contains $N$. Next line contains $N$ space separated numbers. The line, thereafter, contains ${Q}$ , the number of queries to follow. Each of the next ${Q}$ lines contains three positive integer ${i}$, $j$ and ${x}$.

Output Format

For each query display Yes or No as explained above.

Constraints 

$2\leq N\leq2\times10^5$ 

$2\leq Q\leq3\times10^5$ 

$1\leq i,j\leq N$ 

$i\leq j$ 

$1\leq x\leq10^{16}$ 

${{0}\leq$ value of array element $\leq10^{16}$

No 2 consecutive entries in the array will be zero.

Sample Input

4
2 3 4 5
2
1 2 4
1 3 7

Sample Output

Yes
No
"""

import math

def bounded_pow(a, b):
    LIM = 60
    LOG_LIM = math.log(LIM * 2)
    if b * math.log(a) > LOG_LIM:
        return LIM
    return min(pow(a, b), LIM)

def query_divisibility(a, i, j, mod):
    n = len(a)
    nxt = [0] * (n + 1)
    nxt[n] = n
    for k in range(n - 1, -1, -1):
        if a[k] <= 1:
            nxt[k] = k
        else:
            nxt[k] = nxt[k + 1]
    
    if i == j or a[i] <= 1:
        return a[i] % mod == 0
    
    x = a[i]
    i += 1
    tmp = nxt[i]
    j = min(j, tmp)
    p = a[j]
    
    while j > i and p < 60:
        j -= 1
        p = bounded_pow(a[j], p)
    
    return pow(x, p, mod) == 0