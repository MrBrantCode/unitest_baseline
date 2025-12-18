"""
QUESTION:
Write a function called `find_greatest_product` that takes a list of numbers as input and returns the group of three numbers with the greatest product. The list may contain positive and negative integers, floating point numbers, and zeros. If there are multiple groups with the same greatest product, the function should return the group with the smallest sum of its elements. The function should handle lists with at least three elements.
"""

def find_greatest_product(numbers):
    max_product = float('-inf')
    max_group = []
    min_sum = float('inf')
    for i in range(len(numbers)-2):
        for j in range(i+1, len(numbers)-1):
            for k in range(j+1, len(numbers)):
                product = numbers[i] * numbers[j] * numbers[k]
                if product > max_product:
                    max_product = product
                    max_group = [numbers[i], numbers[j], numbers[k]]
                    min_sum = sum(max_group)
                elif product == max_product:
                    group_sum = sum([numbers[i], numbers[j], numbers[k]])
                    if group_sum < min_sum:
                        max_group = [numbers[i], numbers[j], numbers[k]]
                        min_sum = group_sum
    return max_group