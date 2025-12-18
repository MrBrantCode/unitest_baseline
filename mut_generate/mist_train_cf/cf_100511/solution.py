"""
QUESTION:
Write a function called `sum_even_numbers` that takes an integer array as input and returns the sum of all the even elements. The function must use a `SimpleArrayAddition` object and must not modify the original array.
"""

class SimpleArrayAddition:
    def sum_array(self, arr):
        """
        :param arr: a list of integers
        :return: the sum of all the even elements
        """
        sum = 0
        for num in arr:
            if num % 2 == 0:
                sum += num
        return sum

def entance(arr):
    """
    :param arr: a list of integers
    :return: the sum of all the even elements in the list
    """
    saa = SimpleArrayAddition()
    return saa.sum_array(arr)