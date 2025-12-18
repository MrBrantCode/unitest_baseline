"""
QUESTION:
Create a function named `uncommon_elements` that takes a non-empty list of positive whole numbers as input and returns a list of unique numbers that satisfy two conditions:
1. The frequency of the number in the list is more than half the number's value itself.
2. The count of these numbers in the list is a prime number.

If no numbers in the list meet these conditions, the function should return an empty list.
"""

import collections

def uncommon_elements(lst):
    """
    Extract unique whole numbers from the input list that satisfy the conditions
    """
    def is_prime(n):
        """
        Check if n is a prime number
        """
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    count_dict = collections.Counter(lst)

    result = [num for num in count_dict if count_dict[num] > num / 2 and is_prime(count_dict[num])]

    return sorted(result)