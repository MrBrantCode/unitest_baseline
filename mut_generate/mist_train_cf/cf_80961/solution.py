"""
QUESTION:
Write a function `check_product(numbers, prime)` that checks whether the product of numbers in the list `numbers` is divisible by the given prime number `prime`. The function should also identify the index of the first number in the list that is not divisible by `prime`. If there are no such numbers, the function should return -1 as the index. The function should be able to handle large lists efficiently and terminate early when possible.
"""

def check_product(numbers, prime):
    if prime == 0: 
        return "Prime can't be zero!"
    
    product = 1
    not_divisible_index = -1

    for i in range(len(numbers)):
        product *= numbers[i]
        if numbers[i] % prime != 0:
            not_divisible_index = i
            break
            
    product_is_divisible = (product % prime == 0)

    return product_is_divisible, not_divisible_index