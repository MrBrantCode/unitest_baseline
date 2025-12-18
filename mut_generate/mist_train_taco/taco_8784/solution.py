"""
QUESTION:
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python. 

To read more about the functions in this module, check out their documentation here. 

You are given a list of $N$ lowercase English letters. For a given integer $\mbox{K}$, you can select any $\mbox{K}$ indices (assume $\mbox{I}$-based indexing) with a uniform probability from the list.  

Find the probability that at least one of the $\mbox{K}$ indices selected will contain the letter: '$\boldsymbol{\alpha}$'.  

Input Format

The input consists of three lines. The first line contains the integer $N$, denoting the length of the list. The next line consists of $N$ space-separated lowercase English letters, denoting the elements of the list. 

The third and the last line of input contains the integer $\mbox{K}$, denoting the number of
indices to be selected. 

Output Format

Output a single line consisting of the probability that at least one of the $\mbox{K}$ indices selected contains the letter:'$\boldsymbol{\alpha}$'. 

Note: The answer must be correct up to 3 decimal places. 

Constraints

$1\leq N\leq10$

$1\leq K\leq N$

All the letters in the list are lowercase English letters.

Sample Input

4 
a a c d
2

Sample Output

0.8333

Explanation

All possible unordered tuples of length $2$ comprising of indices from $\mbox{I}$ to $\begin{array}{c}A\end{array}$ are:

$(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)$ 

Out of these $\boldsymbol{6}$ combinations, $5$ of them contain either index $\mbox{I}$ or index $2$ which are the indices that contain the letter '$\boldsymbol{\alpha}$'. 

Hence, the answer is $\frac{5}{6}$.
"""

import itertools

def calculate_probability_of_letter(N, letters, K, alpha):
    a = 0
    b = 0
    
    for combination in itertools.combinations(letters, K):
        a += (alpha in combination)
        b += 1
    
    probability = a / b
    return round(probability, 3)