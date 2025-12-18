"""
QUESTION:
Print a sequence a_1, a_2, ..., a_N whose length is N that satisfies the following conditions:

* a_i (1 \leq i \leq N) is a prime number at most 55 555.
* The values of a_1, a_2, ..., a_N are all different.
* In every choice of five different integers from a_1, a_2, ..., a_N, the sum of those integers is a composite number.



If there are multiple such sequences, printing any of them is accepted.

Constraints

* N is an integer between 5 and 55 (inclusive).

Input

Input is given from Standard Input in the following format:


N


Output

Print N numbers a_1, a_2, a_3, ..., a_N in a line, with spaces in between.

Examples

Input

5


Output

3 5 7 11 31


Input

6


Output

2 3 5 7 11 13


Input

8


Output

2 5 7 13 19 37 67 79
"""

def generate_prime_sequence(N):
    # List of precomputed prime numbers that satisfy the conditions
    primes = [11, 31, 41, 61, 71, 101, 131, 151, 181, 191, 211, 241, 251, 271, 281, 311, 331, 401, 421, 431, 461, 491, 521, 541, 571, 601, 631, 641, 661, 691, 701, 751, 761, 811, 821, 881, 911, 941, 971, 991, 1021, 1031, 1051, 1061, 1091, 1151, 1171, 1181, 1201, 1231, 1291, 1301, 1321, 1361, 1381, 1451, 1471, 1481, 1511, 1531]
    
    # Return the first N primes from the list
    return primes[:N]