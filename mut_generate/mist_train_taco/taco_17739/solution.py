"""
QUESTION:
You are given N positive integers A1, A2, ... AN. Find the number of ways to distribute them in 2 groups in such a way that sum of numbers in each group is greater or equal K. The answer can be large so output it modulo 10^9 + 7.

Input
The first line contains two space-separated integers N and K.
The second line contains N space-separated integers: A1, A2, ... AN.

Output
Output one integer - answer for the question modulo 10^9 + 7.

Constraints
 0 < N  ≤ 100
 0 < Ai  ≤ 10^9
 0 < K  ≤ 10^5
 0 < N  ≤ 20 in 28 % of the test data.

SAMPLE INPUT
2 5
6 6


SAMPLE OUTPUT
2
"""

def count_group_distributions(N: int, K: int, A: list) -> int:
    MOD = 1000000007
    
    # Initialize the found array and Kplus
    found = [0] * K
    found[0] = 1
    Kplus = 0
    
    # Early exit if the total sum is less than 2*K
    if sum(A) < 2 * K:
        return 0
    
    # Process each integer in A
    for a in A:
        Kplus = (Kplus * 2) % MOD
        for j in range(max(0, K - a), K):
            Kplus = (Kplus + found[j]) % MOD
        
        for j in range(K - 1, a - 1, -1):
            found[j] = (found[j] + found[j - a]) % MOD
    
    # Calculate the final result
    result = (MOD + Kplus - sum(found) % MOD) % MOD
    return result