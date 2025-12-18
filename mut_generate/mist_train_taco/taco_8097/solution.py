"""
QUESTION:
Given two numbers N and M. Construct maximal number by permuting (changing order) the digits of N, not exceeding M. 
It is allowed to leave N as it is. If there's no Permutation of digits of N which doesn't exceed M, then print -1.
Note : Answer shouldn't have any leading zeroes.
Example 1: 
Input:
N = 123
M = 222
Output:
213
Explanation: There are total 3! permutations 
possible for N = 123, but the only permutation 
that satisfies the given condition is 213.
Example 2: 
Input:
N =  3921
M = 10000
Output:
9321
Explanation: Among all the Possible Permutations,
9321 is Maximum.
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxPerm() which takes two Integers N and M as input parameters and returns the answer.
Expected Time Complexity: O(|N|^{2})
Expected Auxiliary Space: O(|N|)
Constraints:
1 ≤ A, B ≤ 10^{7}
"""

from itertools import permutations

def max_permutation(N: int, M: int) -> int:
    # Generate all permutations of the digits of N
    perm = permutations(str(N))
    
    # Convert permutations to integers and filter those that do not exceed M
    valid_permutations = [int(''.join(p)) for p in perm if int(''.join(p)) <= M]
    
    # Return the maximum valid permutation or -1 if no valid permutations exist
    return max(valid_permutations, default=-1)