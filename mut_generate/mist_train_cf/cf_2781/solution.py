"""
QUESTION:
Create a generator expression that iterates over a given list of integers and yields prime numbers that are not palindromes. The input list can have a maximum length of 1000 and may contain duplicates. Implement the solution using a single line of code with lambda functions and built-in Python functions. Define the solution as a function named `prime_palindrome_generator`.
"""

def prime_palindrome_generator(lst):
    return (num for num in lst 
            if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)) 
            and str(num) != str(num)[::-1])