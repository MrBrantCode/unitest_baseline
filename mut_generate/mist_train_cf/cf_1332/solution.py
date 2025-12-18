"""
QUESTION:
Write a function named find_even_divisible that takes a list of integers as input. The function should return a tuple containing a list of even numbers from the input list that are divisible by both 3 and 5, and the sum of these even numbers. The time complexity of the function should be O(n), where n is the length of the input list, and the space complexity should be O(m), where m is the number of even numbers that are divisible by both 3 and 5.
"""

def find_even_divisible(numbers):
    even_divisible = []
    sum_even_divisible = 0
    for num in numbers:
        if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
            even_divisible.append(num)
            sum_even_divisible += num
    return even_divisible, sum_even_divisible