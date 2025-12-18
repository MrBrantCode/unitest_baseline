"""
QUESTION:
Write a function named `sort_numbers` that takes a list of positive integers as input. The function should return a tuple of two lists: the first list contains prime numbers sorted in ascending order and the second list contains composite numbers sorted in descending order. 

Assume that the input list may contain duplicate numbers and the numbers are not necessarily unique. If the input list is empty, the function should return a tuple of two empty lists.
"""

def sort_numbers(numbers):
    prime_numbers = []
    composite_numbers = []
    
    for num in numbers:
        if num < 2:
            composite_numbers.append(num)
            continue
        
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            prime_numbers.append(num)
        else:
            composite_numbers.append(num)
    
    prime_numbers.sort()
    composite_numbers.sort(reverse=True)
    
    return (prime_numbers, composite_numbers)