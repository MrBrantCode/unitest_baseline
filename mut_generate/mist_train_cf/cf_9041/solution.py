"""
QUESTION:
Create a function `sum_of_even_elements` that takes a list of at least 10 positive integers as input. Calculate the sum of all even elements in the list, but only return the sum if the list has more even elements than odd elements. Otherwise, return "No sum found".
"""

def sum_of_even_elements(lst):
    even_count = 0
    odd_count = 0
    even_sum = 0

    for num in lst:
        if num % 2 == 0:
            even_count += 1
            even_sum += num
        else:
            odd_count += 1

    if even_count > odd_count:
        return even_sum
    else:
        return "No sum found"