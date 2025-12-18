"""
QUESTION:
Implement a function called `generate_and_search_matrix` that takes no arguments. It should configure a three-dimensional matrix representing a combination of arithmetic summation and multiplication of Fibonacci numbers within the range of 0 to 1000, handling potential overflow errors. The function should then implement an algorithm to search for any given number within the matrix and render this tabular structure for observation, ensuring efficient use of time and space complexity.

The function should include the following sub-functions: 

- A function to generate Fibonacci numbers up to 1000
- A function to generate the sum and multiplication matrix
- A function to search for an item in the matrix
- A function to display the matrix

The time complexity for generating matrices should be O(n^2) and the space complexity should also be O(n^2). The time complexity for the search function should be O(1). The function should handle overflow errors within the given range.
"""

import numpy as np

def fib(n):
    fib_nums=[0,1]
    a,b = 0,1
    while b<n:
        a,b = b,a+b
        fib_nums.append(b)
    return fib_nums

def generate_matrix(fib_nums):
    size = len(fib_nums)
    add_matrix = np.zeros((size,size))
    mult_matrix = np.zeros((size,size))
    
    for i in range(size):
        for j in range(size):
            add_matrix[i][j] = fib_nums[i] + fib_nums[j]
            mult_matrix[i][j] = fib_nums[i] * fib_nums[j]
            
    return add_matrix, mult_matrix

def search(matrix, target):
    position = np.where(matrix == target)
    coordinates = list(zip(position[0], position[1]))
    return coordinates

def display(matrix):
    print(matrix)

def generate_and_search_matrix():
    fib_nums = fib(1000)
    add_matrix, mult_matrix = generate_matrix(fib_nums)
    return add_matrix, mult_matrix, search, display

# To use the function, you would do something like this:
add_matrix, mult_matrix, search, display = generate_and_search_matrix()
coordinates = search(add_matrix, 50)
print("Number 50 was found at the following indices: ", coordinates)
display(add_matrix)
display(mult_matrix)