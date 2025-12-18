"""
QUESTION:
Write a function named `sum_even_divisible_by_three` that calculates the sum of all even numbers in a given list that are divisible by 3. The function should not use any built-in sum functions and should have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the list. The list can have a maximum length of 100 elements and may contain duplicate elements.
"""

def sum_even_divisible_by_three(mylist):
    sum = 0
    for num in mylist:
        if num % 2 == 0 and num % 3 == 0:
            sum += num
    return sum