"""
QUESTION:
Write a function `validate_array` that takes an array of integers as input, where each element is greater than 2 and less than 106, and returns True if all elements in the array are prime numbers, and False otherwise. The function should have a time complexity lower than O(n^2) and should not use any built-in prime checking functions.
"""

def validate_array(array):
    def check_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i*i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    for elem in array:
        if not check_prime(elem):
            return False
    return True