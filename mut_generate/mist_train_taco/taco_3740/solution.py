"""
QUESTION:
Leonardo loves primes and created ${q}$ queries where each query takes the form of an integer, $n$. For each $n$, count the maximum number of distinct prime factors of any number in the inclusive range $[1,n]$.

Note: Recall that a prime number is only divisible by ${1}$ and itself, and ${1}$ is not a prime number.  

Example 

$n=100$  

The maximum number of distinct prime factors for values less than or equal to $100$ is $3$.One value with $3$ distinct prime factors is $30$. Another is ${42}$.    

Function Description  

Complete the primeCount function in the editor below.  

primeCount has the following parameters:  

int n: the inclusive limit of the range to check  

Returns  

int: the maximum number of distinct prime factors of any number in the inclusive range $\left[0-n\right]$.  

Input Format

The first line contains an integer, ${q}$, the number of queries. 

Each of the next ${q}$ lines contains a single integer, $n$.

Constraints

$1\leq q\leq10^5$  
$1\leq n\leq10^{18}$  

Sample Input
6
1
2
3
500
5000
10000000000

Sample Output
0
1
1
4
5
10

Explanation

${1}$ is not prime and its only factor is itself. 
$2$ has ${1}$ prime factor, $2$. 
The number $3$ has $1$ prime factor, $3$, $2$ has $1$ and $1$ has $0$ prime factors.
The product of the first four primes is $2\times3\times5\times7=210$.  While higher value primes may be a factor of some numbers, there will never be more than ${4}$ distinct prime factors for a number in this range.
"""

def primeCount(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    maxFacts = -1
    product = 1
    k = 0
    
    while n >= product:
        maxFacts += 1
        product *= primes[k]
        k += 1
    
    return maxFacts