"""
QUESTION:
Write a function `sum_of_even_elements(lst)` that takes a list of at least 10 positive integers as input and returns the sum of all even elements in the list, but only if the list has more even elements than odd elements. If the list does not meet this condition, the function should return "No sum found".
"""

def sum_of_even_elements(lst):
    even_count = 0
    even_sum = 0

    for num in lst:
        if num % 2 == 0:
            even_count += 1
            even_sum += num

    if lst.count(num for num in lst if num % 2 == 0) > lst.count(num for num in lst if num % 2 != 0):
        return even_sum
    else:
        return "No sum found"