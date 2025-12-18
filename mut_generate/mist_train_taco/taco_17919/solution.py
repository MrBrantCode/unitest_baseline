"""
QUESTION:
Shil likes to perform Crazy Operation on an array A1,A2,...AN.

Given an array A1,A2,...AN and permutation P1,P2, ..,PN, a Crazy Operation consists of two parts:  

Perform Operation Bi = Ai for every i in 1..N

Perform Operation Ai = BPi  for every i in 1..N. Here P is a permutation from 1 to N.

Shil asks you to print the resulting array A1, A2,...AN after doing  Crazy Operation on  it , T times.

Input format:
The first line of input consists of two integers N and T. The next line consists of N integers  A1, A2,...AN. The next line consists of permutation P1,P2,...PN.

Output format:
Print the resulting A1,A2,...AN after doing  Crazy operations on it T times.

Constraints:
1≤N≤10^5
1≤T≤10^18
1≤Ai≤10^9

SAMPLE INPUT
5 3
1 2 3 4 5
3 4 5 2 1

SAMPLE OUTPUT
1 4 3 2 5

Explanation

On doing Crazy Operation 1st time resulting array will be (3,4,5,2,1).
On doing second time , resulting array will be (5,2,1,4,3).
On doing third time, resulting array will be (1,4,3,2,5).
"""

def perform_crazy_operation(N, T, A, P):
    """
    Perform the Crazy Operation on the array A for T times using the permutation P.

    Parameters:
    - N (int): The size of the array.
    - T (int): The number of times the Crazy Operation is to be performed.
    - A (list of int): The initial array.
    - P (list of int): The permutation array.

    Returns:
    - list of int: The resulting array after performing the Crazy Operation T times.
    """
    
    # Adjust indices to be 1-based
    A = [0] + A
    P = [0] + P
    
    def apply_permutation(p, x):
        """Helper function to apply permutation p to array x."""
        res = [0] * len(p)
        for i in range(1, len(p)):
            res[i] = x[p[i]]
        return res
    
    # Perform the Crazy Operation T times
    while T > 0:
        if T % 2 == 1:
            A = apply_permutation(P, A)
        P = apply_permutation(P, P)
        T //= 2
    
    # Return the resulting array without the leading 0
    return A[1:]