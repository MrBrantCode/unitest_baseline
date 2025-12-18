"""
QUESTION:
Create a function named `prime_even_list` that takes a 2D list `my_list` as input. Return a list of even numbers from sublists in `my_list` where the sum of each sublist is a prime number greater than 1 and all elements in the sublist are unique.
"""

def prime_even_list(my_list):
    return [x for sublist in my_list for x in sublist if x % 2 == 0 and sum(sublist) > 1 and all(sum(sublist) % i != 0 for i in range(2, int(sum(sublist) ** 0.5) + 1)) and len(set(sublist)) == len(sublist)]