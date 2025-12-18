"""
QUESTION:
James is very naive in Mathematics, He always makes new things out of a given list of integers. Today he is given a list $\boldsymbol{\mbox{L}}$, so he creates a value $\mbox{S}$ out of it.  

$\mbox{S}$ from a given list can be calculated as follows.

value_of_S(list L)
{
    while ((number of elements in L) > 1)
    {
        a = L[0]
        b = L[1]
        delete L[1]
        L[0] = a+b+ab
    }
    return L[0] % 1000000007
}

James has an ample amount of time, so he calculates the values of $\mbox{S}$ for all the permutations of the given list $\boldsymbol{\mbox{L}}$ and finds their average value. Then he asks you to report that value.

Input Format 

The first line contains an integer $N$, the number of integers in the list. 

The second line contains $N$ integral values, $L[0],\ldots,L[N-1]$, separated by single spaces.

Output Format 

Print the floor of the average value.

Constraints 

$2\leq N\leq10^4$ 

$2\leq L[i]\leq10^6$

Sample Input  

2
2 3

Sample Output  

11

Explanation 

The $\mbox{S}$ value corresponding to the two permutations of the given list is $\mbox{11}$.
"""

def calculate_average_S(N, L):
    P = 10**9 + 7
    ret = 1
    for x in L:
        ret = ret * (x + 1) % P
    return (ret - 1) % P