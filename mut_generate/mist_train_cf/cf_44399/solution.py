"""
QUESTION:
Create a function called `get_positive_and_sort` that takes a list of integers as input, filters out the positive numbers, and returns them in ascending order. The function should also include a separate auxiliary function called `swap_elements` that sorts the positive numbers using a bubble sort algorithm, without using the built-in `sort()` or `sorted()` methods. The function should be able to handle lists of varying lengths and should return an empty list if there are no positive numbers in the input list.
"""

def get_positive_and_sort(numbers):
    def swap_elements(n):
        length = len(n)
        for i in range(length):
            for j in range(0, length-i-1):
                if n[j] > n[j+1]:
                    n[j], n[j+1] = n[j+1], n[j]
        return n

    positive_nums = [num for num in numbers if num > 0]
    
    return swap_elements(positive_nums)