"""
QUESTION:
Create a function named `calculate_absolute_difference` that takes a list of tuples as input, where each tuple contains two positive integers. The function should return a new list containing the absolute difference between the first and second element of each tuple, but only if the sum of the elements in the tuple is a prime number. If the sum of the elements in the tuple is not a prime number, return None for that tuple. The function should have a time complexity of O(n), where n is the number of tuples in the input list.
"""

def calculate_absolute_difference(tuples):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = []
    for tup in tuples:
        sum = tup[0] + tup[1]
        if is_prime(sum):
            result.append(abs(tup[0] - tup[1]))
        else:
            result.append(None)
    return result