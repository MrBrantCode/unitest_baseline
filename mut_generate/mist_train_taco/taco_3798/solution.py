"""
QUESTION:
On the Planet AtCoder, there are four types of bases: A, C, G and T. A bonds with T, and C bonds with G.
You are given a letter b as input, which is A, C, G or T. Write a program that prints the letter representing the base that bonds with the base b.

-----Constraints-----
 - b is one of the letters A, C, G and T.

-----Input-----
Input is given from Standard Input in the following format:
b

-----Output-----
Print the letter representing the base that bonds with the base b.

-----Sample Input-----
A

-----Sample Output-----
T
"""

def find_bonding_base(b: str) -> str:
    """
    Returns the base that bonds with the given base b.

    Parameters:
    b (str): A single character string representing one of the bases (A, C, G, T).

    Returns:
    str: A single character string representing the base that bonds with the input base b.
    """
    bonding_pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return bonding_pairs[b]