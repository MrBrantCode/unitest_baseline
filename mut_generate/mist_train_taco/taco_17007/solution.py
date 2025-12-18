"""
QUESTION:
Sona loves numbers. Sona loves only certain type of numbers especially prime numbers. She devised a  new definition for prime numbers. In a given set of positive integer X = {X0,X1,....Xn-1} Xi is prime only if there are no elements in X which are divisors of Xi (except Xi itself).

You are given the set X and find the elements which are prime for this set.

Input format

The first line contains an integer 'N' which denotes the size of the set and the next line contains N spaced integers which represents the elements of the set.

Output format

Print the elements which are prime for this set X

Constraints

1 ≤ N < = 100

1< = X[i] < = 10^6

SAMPLE INPUT
5
10 49 5 3 20

SAMPLE OUTPUT
49 5 3
"""

def find_sona_primes(X):
    """
    Finds the elements in the set X that are considered prime according to Sona's definition.

    Parameters:
    X (list of int): A list of positive integers.

    Returns:
    list of int: A list of integers that are prime according to Sona's definition.
    """
    n = len(X)
    primes = []
    
    for i in range(n):
        count = 0
        for j in range(n):
            if i != j and X[i] % X[j] != 0:
                count += 1
        if count == n - 1:
            primes.append(X[i])
    
    return primes