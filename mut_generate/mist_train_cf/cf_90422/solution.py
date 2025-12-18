"""
QUESTION:
Write a function `find_greatest_product` that takes a list of numbers as input, finds the group of three numbers with the greatest product, and returns this group along with its product. If there are multiple groups with the same greatest product, return the group with the smallest sum of its elements. The list may contain both positive and negative integers, as well as floating point numbers and zeroes, and will always have at least three elements.
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
    return max_group, max_product