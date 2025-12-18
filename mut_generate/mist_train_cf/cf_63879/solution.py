"""
QUESTION:
Create a function named `find_even_numbers` that takes a list of numbers as input and returns a tuple containing a list of even numbers in descending order and their sum. The function should handle non-numeric inputs by ignoring them.
"""

def find_even_numbers(input_list):
    even_numbers = []
    sum_of_evens = 0
    for i in input_list:
        try:
            num = int(i)    # validating if the input is a numeric value
            if num % 2 == 0:
                even_numbers.append(num)
                sum_of_evens += num
        except ValueError:   # handling non-numeric inputs
            continue
            
    even_numbers.sort(reverse=True)
    return (even_numbers, sum_of_evens)