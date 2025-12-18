"""
QUESTION:
There is a sequence whose $n^{\text{th}}$ term is 

$T_n=n^2-(n-1)^2$  

Evaluate the series 

$S_n=T_1+T_2+T_3+\cdots+T_n$ 

Find $S_n\:\text{mod}\:(10^9+7)$.  

Example  

$n=3$  

The series is $1^2-0^2+2^2-1^2+3^2-2^2=1+3+5=9$.  

Function Description  

Complete the summingSeries function in the editor below.  

summingSeries has the following parameter(s):  

int n: the inclusive limit of the range to sum  

Returns  

int: the sum of the sequence, modulo $(10^9+7)$  

Input Format

The first line of input contains $\boldsymbol{\boldsymbol{t}}$, the number of test cases. 

Each test case consists of one line containing a single integer $n$.  

Constraints

$1\leq t\leq10$  
$1\leq n\leq10^{16}$  

Sample Input 0
2
2
1

Sample Output 0
4
1

Explanation 0

Case 1: We have $4=1+3$ 

Case 2: We have $1=1$
"""

def summing_series(n: int) -> int:
    MOD = 1000000007
    return (n * n) % MOD