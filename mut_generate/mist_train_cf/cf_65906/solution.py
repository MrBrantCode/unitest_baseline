"""
QUESTION:
Write a function `divide_array` that takes an array of unique natural numbers as input and divides it into two separate subsets such that the product of each subset's elements is equal to each other. The function should return a tuple consisting of two sets. If such a division is not possible, the function should return None.
"""

def divide_array(arr):
    arr.sort(reverse=True)
    subset1, subset2 = set(), set()
    product1, product2 = 1, 1

    for number in arr:
        if product1 < product2:
            subset1.add(number)
            product1 *= number
        else:
            subset2.add(number)
            product2 *= number

    return (subset1, subset2) if product1 == product2 else None