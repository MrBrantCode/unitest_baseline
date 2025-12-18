"""
QUESTION:
We define $\mbox{P}$ to be a permutation of the first $n$ natural numbers in the range $[1,n]$. Let $p o s[i]$ denote the value at position $\boldsymbol{i}$ in permutation $\mbox{P}$ using $1$-based indexing. 

$\mbox{P}$ is considered to be an absolute permutation if  $|pos[i]-i|=k$ holds true for every $i\in[1,n]$.

Given $n$ and $\boldsymbol{\mbox{k}}$, print the lexicographically smallest absolute permutation $\mbox{P}$.  If no absolute permutation exists, print -1.

Example 

$n=4$ 

$k=2$   

Create an array of elements from $1$ to $n$, $pos=[1,2,3,4]$.  Using $1$ based indexing, create a permutation where every $|pos[i]-i|=k$.  It can be rearranged to $[3,4,1,2]$ so that all of the absolute differences equal $k=2$:  

pos[i]  i   |pos[i] - i|
  3     1        2
  4     2        2
  1     3        2
  2     4        2

Function Description  

Complete the absolutePermutation function in the editor below.  

absolutePermutation has the following parameter(s):  

int n: the upper bound of natural numbers to consider, inclusive  
int k: the absolute difference between each element's value and its index  

Returns   

int[n]: the lexicographically smallest permutation, or $\left[{-1}\right]$ if there is none   

Input Format

The first line contains an integer $\boldsymbol{\boldsymbol{t}}$, the number of queries. 

Each of the next $\boldsymbol{\boldsymbol{t}}$ lines contains $2$ space-separated integers, $n$ and $\boldsymbol{\mbox{k}}$.  

Constraints

$1\leq t\leq10$
$1\leq n\leq10^5$
$0\leq k<n$

Sample Input
STDIN   Function
-----   --------
3       t = 3 (number of queries)
2 1     n = 2, k = 1
3 0     n = 3, k = 0
3 2     n = 3, k = 2

Sample Output
2 1
1 2 3
-1

Explanation

Test Case 0:

Test Case 1:

Test Case 2: 

No absolute permutation exists, so we print -1 on a new line.
"""

def absolute_permutation(n, k):
    if k == 0:
        return list(range(1, n + 1))
    
    if n % (2 * k) != 0:
        return [-1]
    
    result = []
    for i in range(1, n + 1):
        if (i - 1) // k % 2 == 0:
            result.append(i + k)
        else:
            result.append(i - k)
    
    return result