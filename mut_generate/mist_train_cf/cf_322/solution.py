"""
QUESTION:
Write a function named `prime_product` that takes a list of integers as input and returns the product of all prime numbers in the list that are divisible by 4. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the list. Note that the input list may contain duplicate elements and may have a maximum length of 200 elements.
"""

def prime_product(lst):
    product = 1
    for num in lst:
        if num % 4 == 0 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            product *= num
    return product