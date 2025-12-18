"""
QUESTION:
Sasha grew up and went to first grade. To celebrate this event her mother bought her a multiplication table $M$ with $n$ rows and $n$ columns such that $M_{ij}=a_i \cdot a_j$ where $a_1, \dots, a_n$ is some sequence of positive integers.

Of course, the girl decided to take it to school with her. But while she was having lunch, hooligan Grisha erased numbers on the main diagonal and threw away the array $a_1, \dots, a_n$. Help Sasha restore the array!


-----Input-----

The first line contains a single integer $n$ ($3 \leqslant n \leqslant 10^3$), the size of the table. 

The next $n$ lines contain $n$ integers each. The $j$-th number of the $i$-th line contains the number $M_{ij}$ ($1 \leq M_{ij} \leq 10^9$). The table has zeroes on the main diagonal, that is, $M_{ii}=0$.


-----Output-----

In a single line print $n$ integers, the original array $a_1, \dots, a_n$ ($1 \leq a_i \leq 10^9$). It is guaranteed that an answer exists. If there are multiple answers, print any.


-----Examples-----
Input
5
0 4 6 2 4
4 0 6 2 4
6 6 0 3 6
2 2 3 0 2
4 4 6 2 0

Output
2 2 3 1 2 
Input
3
0 99990000 99970002
99990000 0 99980000
99970002 99980000 0

Output
9999 10000 9998
"""

def restore_array_from_multiplication_table(n, M):
    """
    Restores the original array 'a' from the given multiplication table 'M'.

    Parameters:
    n (int): The size of the table (number of rows and columns).
    M (list of list of int): The multiplication table with zeroes on the main diagonal.

    Returns:
    list of int: The restored array 'a'.
    """
    p = (M[0][1] * M[0][2] // M[1][2]) ** 0.5
    a = [int(p)]
    for i in range(1, n):
        a.append(int(M[0][i] // p))
    return a