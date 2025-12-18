"""
QUESTION:
Snuke has one biscuit and zero Japanese yen (the currency) in his pocket. He will perform the following operations exactly K times in total, in the order he likes:

* Hit his pocket, which magically increases the number of biscuits by one.
* Exchange A biscuits to 1 yen.
* Exchange 1 yen to B biscuits.



Find the maximum possible number of biscuits in Snuke's pocket after K operations.

Constraints

* 1 \leq K,A,B \leq 10^9
* K,A and B are integers.

Input

Input is given from Standard Input in the following format:


K A B


Output

Print the maximum possible number of biscuits in Snuke's pocket after K operations.

Examples

Input

4 2 6


Output

7


Input

7 3 4


Output

8


Input

314159265 35897932 384626433


Output

48518828981938099
"""

def max_biscuits_after_operations(K, A, B):
    if B - A <= 2:
        return K + 1
    else:
        kaisu = max(0, (K - A + 1) // 2)
        return K - kaisu * 2 + kaisu * (B - A) + 1