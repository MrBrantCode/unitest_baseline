"""
QUESTION:
Create a function `compute_product_and_sum_of_squares(n)` that computes the product of the numbers from 1 to n and the sum of squares of these numbers. The function should have a time complexity of O(n) and use extra space for optimization.
"""

def compute_product_and_sum_of_squares(n):
    product_list = [1]*(n+1)
    sum_of_squares_list = [0]*(n+1)
  
    for i in range(1, n+1):
        product_list[i] = product_list[i-1]*i
        sum_of_squares_list[i] = sum_of_squares_list[i-1] + i*i
    
    return product_list[n], sum_of_squares_list[n]