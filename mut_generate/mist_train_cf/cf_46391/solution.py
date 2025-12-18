"""
QUESTION:
Develop a Python function named `find_even_numbers` that takes a list of numerical values as input. The function should return a tuple where the first element is a list of even integers from the input list in descending order, and the second element is the sum of all even integers in the list. If the input list contains non-numerical values, the function should raise a TypeError and print an error message for each non-numerical value.
"""

def find_even_numbers(input_list):
    even_numbers = []
    aggregate = 0

    for i in input_list:
        try:
            if i % 2 == 0:
                even_numbers.append(i)
                aggregate += i
        except TypeError:
            print(f"{i} is not numerical.")
    
    even_numbers.sort(reverse=True)
    
    return (even_numbers, aggregate)