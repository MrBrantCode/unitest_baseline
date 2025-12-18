"""
QUESTION:
Sherlock is given an array of $N$ integers ($A_0,A_1...A_{N-1}$ by Watson. Now Watson asks Sherlock how many different pairs of indices $\boldsymbol{i}$ and $j$ exist such that $\boldsymbol{i}$ is not equal to $j$ but $A_i$ is equal to $A_j$.     

That is, Sherlock has to count the total number of pairs of indices $(i,j)$ where  $A_i$=$A_j$ AND $i\neq j$.

Input Format 

The first line contains $\mathbf{T}$, the number of test cases. $\mathbf{T}$ test cases follow. 

Each test case consists of two lines; the first line contains an integer $N$, the size of array, while the next line contains $N$ space separated integers.

Output Format 

For each test case, print the required answer on a different line. 

Constraints 

$1\leq T\leq10$ 

$1\leq N\leq$10^5$$ 

$1\leq A[i]\leq$10^6$$  

Sample input

2
3
1 2 3
3
1 1 2

Sample output   

0
2

Explanation 

In the first test case, no two pair of indices exist which satisfy the given condition. 

In the second test case as A[0] = A[1] = 1, the pairs of indices (0,1) and (1,0) satisfy the given condition.
"""

import collections

def count_matching_pairs(arr):
    """
    Counts the number of pairs of indices (i, j) such that i != j and arr[i] == arr[j].

    Parameters:
    arr (list of int): The input array of integers.

    Returns:
    int: The number of valid pairs.
    """
    # Count the frequency of each element in the array
    counter = collections.Counter(arr)
    
    # Calculate the number of valid pairs
    # For each element with frequency v, the number of pairs is v * (v - 1)
    pairs_count = sum((v * (v - 1)) for v in counter.values())
    
    return pairs_count