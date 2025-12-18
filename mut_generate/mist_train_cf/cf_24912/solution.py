"""
QUESTION:
Write a function `find_triplet(n)` that finds all Pythagorean triplets which sum up to the given number `n`. The function should return a list of tuples, where each tuple contains a Pythagorean triplet. The numbers in each triplet should be distinct and in ascending order.
"""

def find_triplet(n):
    """
    @brief: Finds all Pythagorean triplets which sum upto the given number n
    @param n: the sum which is the given number 
    @return: a list of all Pythagorean triplets which might sum upto n, or an empty list if none are found
    """
    triplets = []
    for a in range(1, n):
        for b in range(a + 1, n - a):
            c = int(n - a - b)
            if (a*a) + (b*b) == (c*c):
                triplets.append((a, b, c))
    return triplets