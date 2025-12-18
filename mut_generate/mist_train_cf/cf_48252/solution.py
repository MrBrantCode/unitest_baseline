"""
QUESTION:
Create a function complex_prime_sort that takes two lists l1 and l2 as input and returns a list of numbers that are both prime and even from the combined lists, sorted in descending order. The function should raise an exception if it encounters a negative number.
"""

def complex_prime_sort(l1: list, l2: list):
    """
    Taking two lists, create a list that sorts numbers that are both prime and even.
    """
    def prime_check(x: int):
        if x < 2 :
            return False
        for i in range(2, int(x/2)+1):
            if x%i==0:
                return False
        return True

    merged_list = sorted(l1 + l2)

    list_prime_even = []

    for num in merged_list:
        if num < 0:
            raise Exception("Negative numbers are not permitted")
        elif num % 2 == 0 and prime_check(num):
            list_prime_even.append(num)
        
    list_prime_even.sort(reverse=True)
    return list_prime_even