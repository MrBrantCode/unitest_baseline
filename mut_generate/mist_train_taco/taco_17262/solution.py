"""
QUESTION:
We have a sequence A of N non-negative integers.
Compute the sum of \prod _{i = 1} ^N \dbinom{B_i}{A_i} over all sequences B of N non-negative integers whose sum is at most M, and print it modulo (10^9 + 7).
Here, \dbinom{B_i}{A_i}, the binomial coefficient, denotes the number of ways to choose A_i objects from B_i objects, and is 0 when B_i < A_i.

-----Constraints-----
 - All values in input are integers.
 - 1 \leq N \leq 2000
 - 1 \leq M \leq 10^9
 - 0 \leq A_i \leq 2000

-----Input-----
Input is given from Standard Input in the following format:
N M
A_1 A_2 \ldots A_N

-----Output-----
Print the sum of \prod _{i = 1} ^N \dbinom{B_i}{A_i}, modulo (10^9 + 7).

-----Sample Input-----
3 5
1 2 1

-----Sample Output-----
8

There are four sequences B such that \prod _{i = 1} ^N \dbinom{B_i}{A_i} is at least 1:
 - B = \{1, 2, 1\}, where \prod _{i = 1} ^N \dbinom{B_i}{A_i} = \dbinom{1}{1} \times \dbinom{2}{2} \times \dbinom{1}{1} = 1;
 - B = \{2, 2, 1\}, where \prod _{i = 1} ^N \dbinom{B_i}{A_i} = \dbinom{2}{1} \times \dbinom{2}{2} \times \dbinom{1}{1} = 2;
 - B = \{1, 3, 1\}, where \prod _{i = 1} ^N \dbinom{B_i}{A_i} = \dbinom{1}{1} \times \dbinom{3}{2} \times \dbinom{1}{1} = 3;
 - B = \{1, 2, 2\}, where \prod _{i = 1} ^N \dbinom{B_i}{A_i} = \dbinom{1}{1} \times \dbinom{2}{2} \times \dbinom{2}{1} = 2.
The sum of these is 1 + 2 + 3 + 2 = 8.
"""

def compute_binomial_product_sum(N, M, A):
    """
    Computes the sum of the product of binomial coefficients for all sequences B of N non-negative integers
    whose sum is at most M, modulo 10^9 + 7.

    Parameters:
    - N (int): The number of elements in the sequence A.
    - M (int): The maximum sum constraint for the sequence B.
    - A (list of int): The sequence of non-negative integers.

    Returns:
    - int: The sum of the product of binomial coefficients modulo 10^9 + 7.
    """
    from functools import reduce

    def modpow(a, n, m):
        if n == 0:
            return 1
        tmp = modpow(a, n // 2, m)
        if n % 2 == 0:
            return tmp * tmp % m
        else:
            return tmp * tmp * a % m

    def modinv(a, m):
        return modpow(a, m - 2, m)

    M = 1000000007
    s = sum(A)
    product = lambda x1, x2: x1 * x2 % M
    
    numerator = reduce(product, list(range(M - s + 1, M + N + 1)))
    denominator = reduce(product, list(range(1, s + N + 1)))
    
    return numerator * modinv(denominator, M) % M