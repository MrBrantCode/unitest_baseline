"""
QUESTION:
start() & end()

These expressions return the indices of the start and end of the substring matched by the group.

Code  

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0

Task 

You are given a string $\mbox{S}$. 

Your task is to find the indices of the start and end of string $\boldsymbol{k}$ in $\mbox{S}$.

Input Format

The first line contains the string $\mbox{S}$. 

The second line contains the string $\boldsymbol{k}$.

Constraints  

$0<len(S)<100$ 

$0<len(k)<len(S)$

Output Format

Print the tuple in this format: (start _index, end _index). 

If no match is found, print (-1, -1).

Sample Input
aaadaa
aa

Sample Output
(0, 1)  
(1, 2)
(4, 5)
"""

import re

def find_substring_indices(S: str, k: str) -> list:
    indices = []
    m = re.search(k, S)
    ind = 0
    
    if not m:
        return [(-1, -1)]
    
    while m:
        start_index = ind + m.start()
        end_index = ind + m.start() + len(k) - 1
        indices.append((start_index, end_index))
        ind += m.start() + 1
        m = re.search(k, S[ind:])
    
    return indices