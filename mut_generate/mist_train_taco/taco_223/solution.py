"""
QUESTION:
Recently you invented a brand-new definition of prime numbers. For a given set of positive integers S let's call X a prime if there are no elements in S which are divisors of X (except  X itself).

You are given a set S. Find elements in it which are prime numbers for this set.

Input
The first line contains one integer N - size of the set S.
The second line contains N space-separated integers - elements of S. All the numbers are pairwise different.

Output
Output one line: elements of S which are prime numbers for this set in the order they occur in the input. Separate them by whitespaces.

Constraints
N ≤ 100
1 ≤ S[i] ≤ 10^6 (1 ≤ i ≤ n)

SAMPLE INPUT
5
10 5 3 15 16

SAMPLE OUTPUT
 5 3 16
"""

def find_prime_elements(S):
    """
    Finds elements in the set S which are prime numbers according to the new definition.

    Parameters:
    S (list of int): The set of positive integers.

    Returns:
    list of int: Elements of S which are prime numbers for this set.
    """
    prime_elements = []
    for i in range(len(S)):
        is_prime = True
        for j in range(len(S)):
            if i != j and S[i] % S[j] == 0:
                is_prime = False
                break
        if is_prime:
            prime_elements.append(S[i])
    return prime_elements