"""
QUESTION:
Create a function `process_array` that takes a list of mixed data types (integers, floats, and strings) as input. Invert the order of the input list without using any built-in methods. Then, for the inverted list, print each element's type. Additionally, find the sum of the integer elements at even indices in ascending order and the integer elements at odd indices in descending order. Return the sum of the integers.
"""

def process_array(arr):
    # Invert the order of the input list without using any built-in methods
    inverted_arr = [None] * len(arr)
    for i in range(len(arr)):
        inverted_arr[-i - 1] = arr[i]
        
    # Print each element's type in the inverted list
    for elem in inverted_arr:
        print(f'{elem} of type {type(elem)}')
        
    # Find the sum of the integer elements at even indices in ascending order and the integer elements at odd indices in descending order
    even_indices = [elem for idx, elem in enumerate(inverted_arr) if idx % 2 == 0 and isinstance(elem, int)]
    odd_indices = [elem for idx, elem in enumerate(inverted_arr) if idx % 2 != 0 and isinstance(elem, int)]

    even_indices.sort()
    odd_indices.sort(reverse=True)

    return sum(even_indices) + sum(odd_indices)