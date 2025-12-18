"""
QUESTION:
Write a function `extract_and_aggregate_even_numbers` that takes a string as input and returns a list of numerical characters and the sum of all even numbers in the string. The function should isolate numerical characters embedded within the string, convert them to integers, and calculate the aggregate of all even numbers present in the string. The function should return both the list of numerical characters and the sum of even numbers.
"""

def extract_and_aggregate_even_numbers(string):
    digits = [int(s) for s in string if s.isdigit()]
    even_nums_sum = sum(d for d in digits if d % 2 == 0)
    
    return digits, even_nums_sum