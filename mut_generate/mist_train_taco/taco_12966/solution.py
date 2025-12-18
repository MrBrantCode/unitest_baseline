"""
QUESTION:
There is an array of $n$ integers. There are also $2$ disjoint sets, $\mbox{A}$ and $\mbox{B}$, each containing $m$ integers. You like all the integers in set $\mbox{A}$ and dislike all the integers in set $\mbox{B}$. Your initial happiness is $\mbox{o}$. For each $\boldsymbol{i}$ integer in the array, if $i\in A$, you add $\mbox{I}$ to your happiness. If $i\in B$, you add $-1$ to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.  

Note: Since $\mbox{A}$ and $\mbox{B}$ are sets, they have no repeated elements. However, the array might contain duplicate elements.  

Constraints 

$1\leq n\leq10^5$ 

$1\leq m\leq10^5$ 

$1\leq\textit{Any integer in the input}\leq10^9$  

Input Format

The first line contains integers $n$ and $m$ separated by a space. 

The second line contains $n$ integers, the elements of the array. 

The third and fourth lines contain $m$ integers, $\mbox{A}$ and $\mbox{B}$, respectively.

Output Format

Output a single integer, your total happiness.

Sample Input
3 2
1 5 3
3 1
5 7

Sample Output
1

Explanation

You gain $\mbox{I}$ unit of happiness for elements $3$ and $\mbox{I}$ in set $\mbox{A}$. You lose $\mbox{I}$ unit for $5$ in set $\mbox{B}$. The element $7$ in set $\mbox{B}$ does not exist in the array so it is not included in the calculation. 

Hence, the total happiness is $2-1=1$.
"""

def calculate_happiness(n, m, arr, A, B):
    """
    Calculate the final happiness based on the elements in the array and the sets A and B.

    Parameters:
    n (int): The number of elements in the array.
    m (int): The number of elements in each set (A and B).
    arr (list): The array of integers.
    A (set): The set of integers that increase happiness.
    B (set): The set of integers that decrease happiness.

    Returns:
    int: The final happiness.
    """
    happiness = 0
    for el in arr:
        if el in A:
            happiness += 1
        elif el in B:
            happiness -= 1
    return happiness