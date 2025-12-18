"""
QUESTION:
Write a function `greatest_multiple_of_three` that takes a list of numbers as input and prints the largest number that is a multiple of 3. If no such number exists in the list, print "No multiple of 3 found".
"""

def greatest_multiple_of_three(numbers):
    multiples_of_three = [num for num in numbers if num % 3 == 0]
    if multiples_of_three:
        return max(multiples_of_three)
    else:
        return "No multiple of 3 found"