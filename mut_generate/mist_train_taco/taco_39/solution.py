"""
QUESTION:
Consider sequences \{A_1,...,A_N\} of length N consisting of integers between 1 and K (inclusive).
There are K^N such sequences. Find the sum of \gcd(A_1, ..., A_N) over all of them.
Since this sum can be enormous, print the value modulo (10^9+7).
Here \gcd(A_1, ..., A_N) denotes the greatest common divisor of A_1, ..., A_N.

-----Constraints-----
 - 2 \leq N \leq 10^5
 - 1 \leq K \leq 10^5
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N K

-----Output-----
Print the sum of \gcd(A_1, ..., A_N) over all K^N sequences, modulo (10^9+7).

-----Sample Input-----
3 2

-----Sample Output-----
9

\gcd(1,1,1)+\gcd(1,1,2)+\gcd(1,2,1)+\gcd(1,2,2)+\gcd(2,1,1)+\gcd(2,1,2)+\gcd(2,2,1)+\gcd(2,2,2)=1+1+1+1+1+1+1+2=9
Thus, the answer is 9.
"""

def sum_of_gcd_sequences(N: int, K: int) -> int:
    """
    Calculate the sum of the greatest common divisors (GCD) of all sequences of length N
    consisting of integers between 1 and K (inclusive), modulo (10^9 + 7).

    Parameters:
    N (int): The length of the sequences.
    K (int): The maximum integer value in the sequences.

    Returns:
    int: The sum of the GCDs of all sequences, modulo (10^9 + 7).
    """
    D = [0] * (K + 1)
    D[K] = 1
    mod = 10 ** 9 + 7
    
    for i in range(K, 0, -1):
        D[i] = pow(K // i, N, mod)
        for j in range(2 * i, K + 1, i):
            D[i] = (D[i] - D[j]) % mod
    
    c = 0
    for i in range(1, len(D)):
        c += D[i] * i
    
    return c % mod