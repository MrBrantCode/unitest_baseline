"""
QUESTION:
Write a program which reads a sequence of integers $A = \\{a_0, a_1, ..., a_{n-1}\\}$ and reverse specified elements by a list of the following operation:

* reverse($b, e$): reverse the order of $a_b, a_{b+1}, ..., a_{e-1}$

Constraints

* $1 \leq n \leq 1,000$
* $-1,000,000,000 \leq a_i \leq 1,000,000,000$
* $1 \leq q \leq 1,000$
* $0 \leq b < e \leq n$

Input

The input is given in the following format.


$n$
$a_0 \; a_1 \; ...,\; a_{n-1}$
$q$
$b_1 \; e_1$
$b_2 \; e_2$
:
$b_{q} \; b_{q}$


In the first line, $n$ (the number of elements in $A$) is given. In the second line, $a_i$ (each element in $A$) are given. In the third line, the number of queries $q$ is given and each query is given by two integers $b_i \; e_i$ in the following $q$ lines.

Output

Print all elements of $A$ in a line after performing the given operations. Put a single space character between adjacency elements and a newline at the end of the last element.

Example

Input

8
1 2 3 4 5 6 7 8
2
1 6
3 8


Output

1 6 5 8 7 2 3 4
"""

def reverse_elements_in_sequence(n, a, queries):
    """
    Reverses specified elements in a sequence based on given queries.

    Parameters:
    - n (int): The number of elements in the sequence.
    - a (list of int): The sequence of integers.
    - queries (list of tuple): A list of tuples where each tuple contains two integers (b, e) representing the start and end indices for the reverse operation.

    Returns:
    - list of int: The modified sequence after performing all the reverse operations.
    """
    for (b, e) in queries:
        a[b:e] = a[b:e][::-1]
    return a