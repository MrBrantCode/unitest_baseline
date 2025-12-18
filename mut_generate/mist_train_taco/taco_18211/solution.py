"""
QUESTION:
Shil has an array of N elements A1 , A2, ... ,AN . He also has an integer K. He wants to find out value of Square Sum for every i from 1 to N-K+1.
The value of Square Sum for certain i is defined as  Σ1≤ j ≤ K (j^2 Ai+j-1).

Input:
First line of input consists of two integers N and K. Next line consists of N integers A1 , A2, ... ,AN.

Output:
Output N-K+1 integers where ith integer corresponds to Square Sum of i. Print Square Sum modulus 10^9+7.

Constraints:
1≤ K ≤ N ≤ 10^6 
1≤ Ai ≤ 10^9

SAMPLE INPUT
6 3
6 9 10 10 4 6 

SAMPLE OUTPUT
132 139 86 80
"""

def calculate_square_sums(N, K, A):
    modN = 10**9 + 7
    S_1 = 0
    S_2 = 0
    S_3 = 0

    # Initialize the first window
    for i in range(K):
        S_3 = (S_3 + A[i]) % modN
        S_2 = (S_2 + (i + 1) * A[i]) % modN
        S_1 = (S_1 + (i + 1)**2 * A[i]) % modN
    
    output = [S_1]

    # Slide the window across the array
    for i in range(N - K):
        S_1 = (S_1 + (K + 1)**2 * A[K + i] - 2 * (S_2 + (K + 1) * A[K + i]) + S_3 + A[K + i]) % modN
        output.append(S_1)
        S_2 = (S_2 + (K + 1) * A[K + i] - (S_3 + A[K + i])) % modN
        S_3 = (S_3 + A[K + i] - A[i]) % modN
    
    return output