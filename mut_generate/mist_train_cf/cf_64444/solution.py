"""
QUESTION:
Design a function named `product_of_digits` that takes one argument, which can be either a positive integer or a list of positive integers, and returns the product of the digits of the input integer(s). If the input is a list, the function should return a list of products, one for each integer in the input list.
"""

from typing import List, Union

def product_of_digits(input_array: Union[int, List[int]]) -> Union[int, List[int]]:
    def find_product(num: int) -> int:
        product = 1
        while(num > 0):
            product *= num % 10
            num = num // 10
        return product
    
    if isinstance(input_array, list):
        return [find_product(num) for num in input_array]
    else:
        return find_product(input_array)