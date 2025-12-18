"""
QUESTION:
Chef has a sequence of positive integers $A_1, A_2, \ldots, A_N$. He wants to choose some elements of this sequence (possibly none or all of them) and compute their MEX, i.e. the smallest positive integer which does not occur among the chosen elements. For example, the MEX of $[1, 2, 4]$ is $3$.
Help Chef find the largest number of elements of the sequence $A$ which he can choose such that their MEX is equal to $M$, or determine that it is impossible.

-----Input-----
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

-----Output-----
For each test case, print a single line containing one integer ― the maximum number of elements Chef can choose, or $-1$ if he cannot choose elements in such a way that their MEX is $M$.

-----Constraints-----
- $1 \le T \le 100$
- $2 \le M \le N \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^6$

-----Example Input-----
1
3 3
1 2 4

-----Example Output-----
3

-----Explanation-----
Example case 1: The MEX of whole array is 3. Hence, we can choose all the elements.
"""

from collections import Counter

def max_elements_with_mex(N, M, A):
    A.sort()
    flag = 1
    
    # Check if all elements from 1 to M-1 are present
    for i in range(1, M):
        if i not in A:
            flag = 0
            break
    
    if flag == 0:
        return -1
    
    # Count occurrences of elements in the array
    d1 = Counter(A)
    value = d1.get(M, 0)
    
    # Return the maximum number of elements that can be chosen
    return N - value