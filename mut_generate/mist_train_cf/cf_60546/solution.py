"""
QUESTION:
Write a function named `get_positive_and_sort` that takes a list of integers as input, filters out the positive integers, sorts them in ascending order, and returns the sorted list. The sorting must be done using a custom `swap_elements` function, which should implement a sorting algorithm without using built-in sort functions like `sort()` or `sorted()`.
"""

def get_positive_and_sort(l: list) -> list:
    positive_elements = [num for num in l if num > 0] # filter positive numbers

    def swap_elements(n: list) -> list:
        length = len(n)
        for i in range(length): 
            for j in range(0, length-i-1): 
                if n[j] > n[j+1]: 
                    n[j], n[j+1] = n[j+1], n[j] # swap if the element found is greater than the next element
        return n

    return swap_elements(positive_elements) # return sorted positive numbers