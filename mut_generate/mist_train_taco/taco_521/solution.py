"""
QUESTION:
You are given an integer, $N$. Write a program to determine if $N$ is an element of the Fibonacci sequence.  

The first few elements of the Fibonacci sequence are $0,1,1,2,3,5,8,13,\cdots$. A Fibonacci sequence is one where every element is a sum of the previous two elements in the sequence. The first two elements are ${0}$ and ${1}$. 

Formally: 

$\begin{aligned}&\textit{fib}_0=0\\ &\textit{fib}_1=1\\ &\vdots\\ &\textit{fib}_n=fib_{n-1}+fib_{n-2}\forall n>1\end{aligned}$

Function Description   

Complete the isFibo function in the editor below.   

isFibo has the following parameters: 

- int n: the number to check   

Returns 

- string: either IsFibo or IsNotFibo

Input Format 

The first line contains ${t}}$, number of test cases. 

${t}}$ lines follow. Each line contains an integer $n$.

Constraints 

$1\leq t\leq10^5$ 

$1\leq n\leq10^{10}$

Sample Input  

STDIN   Function
-----   --------
3       t = 3
5       n = 5
7       n = 7
8       n = 8

Sample Output  

IsFibo
IsNotFibo
IsFibo

Explanation 

$5$ is a Fibonacci number given by ${fib}_5=3+2$ 

$7$ is not a Fibonacci number 

$8$ is a Fibonacci number given by ${fib}_6=5+3$  

Time Limit 

The time limit for this challenge is given here.
"""

def is_fibonacci(n: int) -> str:
    # Precompute Fibonacci numbers up to the maximum constraint
    fibonacci = [0, 1]
    while fibonacci[-1] <= 10 ** 10:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    # Check if n is in the precomputed Fibonacci list
    if n in fibonacci:
        return "IsFibo"
    else:
        return "IsNotFibo"