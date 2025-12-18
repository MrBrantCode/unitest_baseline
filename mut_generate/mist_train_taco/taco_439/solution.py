"""
QUESTION:
You are given an array of integers. Your task is to sort odd numbers within the array in ascending order, and even numbers in descending order.

Note that zero is an even number. If you have an empty array, you need to return it.


For example:
```
[5, 3, 2, 8, 1, 4]  -->  [1, 3, 8, 4, 5, 2]

odd numbers ascending:   [1, 3,       5   ]
even numbers descending: [      8, 4,    2]
```
"""

def sort_array_by_parity(arr):
    # Separate odd and even numbers
    odd_numbers = sorted((x for x in arr if x % 2 != 0))
    even_numbers = sorted((x for x in arr if x % 2 == 0), reverse=True)
    
    # Create a result list by replacing odd and even numbers in their original positions
    result = []
    odd_index = 0
    even_index = 0
    
    for x in arr:
        if x % 2 == 0:
            result.append(even_numbers[even_index])
            even_index += 1
        else:
            result.append(odd_numbers[odd_index])
            odd_index += 1
    
    return result