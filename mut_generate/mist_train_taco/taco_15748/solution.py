"""
QUESTION:
Given an array of integers and a positive integer $\boldsymbol{\mbox{k}}$, determine the number of $(i,j)$ pairs where $i<j$ and $ar[i]$ + $ar[j]$ is divisible by $\boldsymbol{\mbox{k}}$.  

Example  

$ar=[1,2,3,4,5,6]$ 

$k=5$   

Three pairs meet the criteria:  $[1,4],[2,3],$ and $[4,6]$.  

Function Description

Complete the divisibleSumPairs function in the editor below.   

divisibleSumPairs has the following parameter(s):  

int n: the length of array $\boldsymbol{ar}$  
int ar[n]: an array of integers  
int k: the integer divisor   

Returns 

-   int: the number of pairs  

Input Format

The first line contains $2$ space-separated integers, $n$ and $\boldsymbol{\mbox{k}}$. 

The second line contains $n$ space-separated integers, each a value of $arr\left[i\right]$.  

Constraints

$2\leq n\leq100$
$1\leq k\leq100$
$1\leq ar[i]\leq100$

Sample Input
STDIN           Function
-----           --------
6 3             n = 6, k = 3
1 3 2 6 1 2     ar = [1, 3, 2, 6, 1, 2]

Sample Output
 5

Explanation

Here are the $5$ valid pairs when $k=3$: 

$(0,2)\rightarrow ar[0]+ar[2]=1+2=3$   
$(0,5)\rightarrow ar[0]+ar[5]=1+2=3$   
$(1,3)\rightarrow ar[1]+ar[3]=3+6=9$   
$(2,4)\rightarrow ar[2]+ar[4]=2+1=3$   
$(4,5)\rightarrow ar[4]+ar[5]=1+2=3$
"""

def divisible_sum_pairs(n, ar, k):
    result = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                result += 1
    return result