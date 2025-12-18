"""
QUESTION:
Integer sequence $\boldsymbol{a}$ having length $2n+2$ is defined as follows:

$a_{0}=0$
$a_{1}=C$
$a_{i+2}=(a_{i+1}+a_i)\ \text{\% M}$, where $0\leq i<2n$

Write a function generator, $gen$, to generate the remaining values for $a_2$ through $a_{2n+1}$. The values returned by $gen$ describe two-dimensional vectors $v_1\ldots v_n$, where each sequential pair of values describes the respective $\boldsymbol{x}$ and $y$ coordinates for some vector $\boldsymbol{\nu}$ in the form $x_1,y_1,x_2,y_2,\ldots,x_n,y_n$. In other words, $v_1=(a_2,a_3),v_2=(a_4,a_5),...,v_n=(a_{2n},a_{2n+1})$.

Let $\mbox{S}$ be the set of scalar products of $v_i$ and $v_j$ for each $1\leq i,j\leq n$, where $i\neq j$.
Determine the number of different residues in $\mbox{S}$ and print the resulting value modulo $\mbox{M}$.

Input Format

A single line of three space-separated positive integers: $\mbox{C}$ (the value of $a_1$), $\mbox{M}$ (the modulus), and $n$ (the number of two-dimensional vectors), respectively.

Constraints

$1\leq C\leq10^9$
$1\leq M\leq10^9$ 
$1\leq n\leq3\times10^5$

Output Format

Print a single integer denoting the number of different residues $\textbf{\% M}$ in $\mbox{S}$.

Sample Input
4 5 3

Sample Output
2

Explanation

Sequence $a=a_0,a_1,(a_1+a_0)\text{\%}M,(a_2+a_1)\text{\%}M,...,(a_{2n}+a_{2n-1})\text{\%}M\}$ 
$=\{0,\ 4,\ (4+0)\%5,\ (4+4)\%5,\ (3+4)\%5,\ (2+3)\%5,\ (0+2)\%5,\ (2+0)\%5\}$
$=\{0,4,4,3,2,0,2,2\}$.

This gives us our vectors: $v_1=(4,3)$, $v_2=(2,0)$, and $v_3=(2,2)$.  

Scalar product $S_0(v_1,v_2)=8$. 

Scalar product $S_2(v_2,v_3)=4$. 

Scalar product $S_0(v_1,v_3)=14$. 

There are $2$ residues $\%5$ in $\mbox{S}$ (i.e.: $3$ and $4$), so we print the result of $2\%5$ (which is $2$).
"""

def count_distinct_residues(C, M, n):
    if n == 1:
        return 0
    
    arr = [0] * (2 * n + 2)
    arr[0] = 0
    arr[1] = C
    
    # Generate the sequence a
    for i in range(2, 2 * n + 2):
        arr[i] = (arr[i - 1] + arr[i - 2]) % M
    
    residues = set()
    
    # Calculate scalar products and collect residues
    for i in range(2, 2 * n - 2, 2):
        temp1 = (arr[i] * arr[i + 2] + arr[i + 1] * arr[i + 3]) % M
        residues.add(temp1)
        temp2 = (arr[i] * arr[i + 4] + arr[i + 1] * arr[i + 5]) % M
        residues.add(temp2)
    
    # Handle the last pair of vectors
    temp = (arr[2 * n - 2] * arr[2 * n] + arr[2 * n - 1] * arr[2 * n + 1]) % M
    residues.add(temp)
    
    return len(residues)