"""
QUESTION:
Write a function named `check_product_subset` that takes two parameters, a list of positive integers and a target integer. The function should return True if there exists a subset of the integers (not necessarily consecutive) in the list whose product equals the target integer, and False otherwise. The solution should not use division, should work when the list contains zeroes, and should be time-efficient without generating all possible permutations of the list.
"""

def check_product_subset(lst, target):
    length = len(lst)
    for i in range(length):
        subsets = combinations(lst, i+1)
        for subset in subsets:
            product = 1
            for number in subset:
                product *= number
            if product == target:
                return True
    return False