"""
QUESTION:
Suppose you have a binary array B of length N.  
A sequence x_{1}, x_{2}, \ldots, x_{k} is called *good* with respect to B if it satisfies the following conditions:
1 ≤ x_{1} < x_{2} < \ldots < x_{k} ≤ N+1
For *every* pair (i, j) such that 1 ≤ i < j ≤ k, the subarray B[x_{i}: x_{j}-1] contains (j-i) more ones than zeros.
- That is, if B[x_{i} : x_{j}-1] contains c_{1} ones and c_{0} zeros, then c_{1} - c_{0} = j-i must hold.

Here, B[L: R] denotes the subarray consisting of elements [B_{L}, B_{L+1}, B_{L+2}, \ldots, B_{R}].  
Note that in particular, a sequence of size 1 is always *good*.

For example, suppose B = [0,1,1,0,1,1]. Then,
The sequence [1,4,7] is a *good* sequence. The subarrays that need to be checked are B[1:3], B[1:6] and B[4:6], which all satisfy the condition.
The sequence [1, 5] is not *good*, because B[1:4] = [0, 1, 1, 0] contains an equal number of zeros and ones (when it should contain one extra 1).

Alice gave Bob a binary array A of size N and asked him to find the longest sequence that is *good* with respect to A. Help Bob find one such sequence.  
If multiple possible longest sequences exist, you may print any of them.
 
------ Input Format ------ 

- The first line of input will contain a single integer T, denoting the number of test cases.
- Each test case consists of two lines of input.
- The first line of each test case contains a single integer N — the size of the binary array.
- The second line contains N space-separated numbers — A_{1} , A_{2} , \ldots , A_{N}.

------ Output Format ------ 

Each test case requires two lines of output:
- First, print on a new line a single integer K — the maximum length of a sequence that is good with respect to A
- On the next line, print K space-separated integers in increasing order, denoting the indices of one such sequence.

If there are multiple possible good sequences with maximum size, output any of them.

------ Constraints ------ 

$1 ≤ T ≤ 10^{5}$
$1 ≤ N ≤ 10^{5}$
$0 ≤ A_{i} ≤ 1$
- The sum of $N$ over all test cases won't exceed $10^{6}$.

----- Sample Input 1 ------ 
4
6
0 1 1 0 1 1
5
0 1 0 1 0
4
1 1 1 1
3
1 0 0
----- Sample Output 1 ------ 
4
2 5 6 7
2
4 5
5
1 2 3 4 5
2
1 2
----- explanation 1 ------ 
Test case $1$: We have $A = [0, 1, 1, 0, 1, 1]$. The sequence $[2, 5, 6, 7]$ requires us to check $6$ subarrays:
- $A[2:4] = [1, 1, 0]$ which has $c_{1} - c_{0} = 1$ and corresponds to $i = 1, j = 2$
- $A[2:5] = [1, 1, 0, 1]$ which has $c_{1} - c_{0} = 2$ and corresponds to $i = 1, j = 3$
- $A[2:6] = [1, 1, 0, 1, 1]$ which has $c_{1} - c_{0} = 3$ and corresponds to $i = 1, j = 4$
- $A[5:5] = [1]$, which has $c_{1} - c_{0} = 1$ and corresponds to $i = 2, j = 3$
- $A[5:6] = [1, 1]$, which has $c_{1} - c_{0} = 2$ and corresponds to $i = 2, j = 4$
- $A[6:6] = [1]$, which has $c_{1} - c_{0} = 1$ and corresponds to $i = 3, j = 4$

As you can see, all $6$ pairs satisfy the condition.

Test case $2$: The only subarray that needs to be checked is $A[4:4] = [1]$, which has $c_{1} - c_{0} = 1$ as needed. It can be verified that no good sequence of length greater than $2$ exists.
"""

from collections import defaultdict

def find_longest_good_sequence(arr):
    n = len(arr)
    
    # Convert 0s to -1s for easier prefix sum calculation
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1
    
    # Calculate prefix sums
    pSum = [0]
    for i in range(n):
        pSum.append(pSum[-1] + arr[i])
    
    # Dictionaries to store lengths and last positions
    l = defaultdict(int)
    last = defaultdict(int)
    
    # Arrays to store ending lengths and links
    ending_at = [0] * (n + 1)
    link = [-1] * (n + 1)
    
    # Fill the dictionaries and arrays
    for i in range(n + 1):
        curr = l[pSum[i] - 1] + 1
        ending_at[i] = curr
        if curr > 1:
            link[i] = last[pSum[i] - 1]
        l[pSum[i]] = curr
        last[pSum[i]] = i
    
    # Find the maximum length of a good sequence
    max_length = max(ending_at)
    
    # Find the longest good sequence
    for i in range(n, 0, -1):
        if ending_at[i] == max_length:
            curr = i
            res = []
            while True:
                res.append(curr + 1)
                if link[curr] == -1:
                    break
                curr = link[curr]
            res.reverse()
            return max_length, res
    
    # If no sequence is found (which shouldn't happen), return default values
    return 0, []