"""
QUESTION:
Create a function named `square_odd_numbers` that takes a list of integers as input and prints the squared value of each odd number in the list. For even numbers, print "Skipped" instead. The function should also return the sum of the squared odd numbers.
"""

def square_odd_numbers(lst):
    sum_squared_odd = 0
    for num in lst:
        if num % 2 != 0:  
            squared_num = num ** 2
            sum_squared_odd += squared_num
            print(squared_num)
        else:
            print("Skipped")
    print("Sum of squared odd numbers:", sum_squared_odd)
    return sum_squared_odd