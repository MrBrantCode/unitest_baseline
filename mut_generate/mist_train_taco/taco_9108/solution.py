"""
QUESTION:
Sam is playing with an array, $\mbox{A}$, of $N$ positive integers. Sam writes a list, $\mbox{S}$, containing all $\mbox{A}$'s contiguous subarrays, and then replaces each subarray with its respective maximum element.

For example, consider the following $\mbox{A}$ where $N=3$: 

$A=\{1,2,3\}$ 

Subarrays of $\mbox{A}$: $S_{initial}=\{\{1\},\{2\},\{3\},\{1,2\},\{2,3\},\{1,2,3\}\}$ 

Updated (Maximum) Subarrays: $S_{maximums}=\{\{1\},\{2\},\{3\},\{2\},\{3\},\{3\}\}$

Help Sam determine how many numbers in $S_{maximums}$ are greater than $\mbox{K}$.

Input Format

The first line contains a single integer, $\mathbf{T}$ (the number of test cases). Each test case is described over two lines: 

The first line of each test case contains two space-separated integers, $N$ (the number of elements in array $\mbox{A}$) and $\mbox{K}$, respectively. 

The second line of each test case contains $N$ space-separated integers describing the elements in $\mbox{A}$.  

Constraints 

$1\leq T\leq10^5$ 

$1\leq N\leq2\times10^5$ 

$1\leq A_i\leq10^9$ 

$0\leq K\leq10^9$ 

$\textit{The sum of N over all test cases does not expressed 10^6}$.  

Output Format

For each test case, print the number of $\textit{maximums}>K$ in $S_{maximums}$ on a new line.

Sample Input
2
3 2
1 2 3 
3 1 
1 2 3 

Sample Output
3
5

Explanation

Both test cases use the same $\mbox{A}$ as described in the Problem Statement, so $S_{maximums}=\{\{1\},\{2\},\{3\},\{2\},\{3\},\{3\}\}$ for both test cases.

Test Case 0: $K=2$ 

$S_{maximums}$ has $3$ elements $>2$, so we print $3$.   

Test Case 1: $K=1$ 

$S_{maximums}$ has $5$ elements ${>1}$, so we print $5$.
"""

def count_maximums_greater_than_k(a, k):
    """
    Counts the number of maximums in all contiguous subarrays of `a` that are greater than `k`.

    Parameters:
    a (list of int): The array of integers.
    k (int): The threshold value to compare against.

    Returns:
    int: The count of maximums greater than `k`.
    """
    bad = 0
    streak = 0
    for x in a:
        if x > k:
            streak = 0
        else:
            streak += 1
            bad += streak
    total_subarrays = len(a) * (len(a) + 1) // 2
    return total_subarrays - bad