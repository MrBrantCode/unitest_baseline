"""
QUESTION:
Create a function named `append_elements` that takes an array and a number of elements to append at the end. The function should return the updated array if the array is not empty, the number of elements to append is a prime number, and the sum of the elements in the array after appending is a perfect square. Otherwise, return an error message. The function should have a time complexity of O(n), where n is the length of the array.
"""

def append_elements(array, num_elements):
    if len(array) == 0:
        return "Array is empty"
    
    if num_elements <= 1 or any(num_elements % i == 0 for i in range(2, int(num_elements**0.5) + 1)):
        return "Number of elements to append is not a prime number"

    array += [i for i in range(1, num_elements + 1)]
    
    sum_array = sum(array)
    sqrt_sum = int(sum_array ** 0.5)
    
    if sqrt_sum * sqrt_sum == sum_array:
        return array
    else:
        return "Sum of elements in the array after appending is not a perfect square"