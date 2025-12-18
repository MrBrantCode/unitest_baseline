"""
QUESTION:
Create a function `process_list` that takes a list of integers as input and iterates through each element along with its index position. Skip the iteration if the element is divisible by both 3 and 5, and keep track of the total number of iterations skipped. For each element, check if it's a prime number and print whether it's prime or not. Calculate and print the sum of all prime numbers in the list. The function should handle cases where the list contains negative integers.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def process_list(input_list):
    """
    Process a list of integers, skipping elements divisible by both 3 and 5.
    Print whether each element is prime or not and calculate the sum of prime numbers.
    
    Args:
    input_list (list): A list of integers.
    
    Returns:
    None
    """
    skipped_iterations = 0
    prime_sum = 0

    for i, element in enumerate(input_list):
        if element % 3 == 0 and element % 5 == 0:
            skipped_iterations += 1
            continue
        
        print("Index:", i, "Element:", element)
        
        if is_prime(abs(element)):
            print(element, "is prime")
            prime_sum += element
        else:
            print(element, "is not prime")

    print("Total skipped iterations:", skipped_iterations)
    print("Sum of prime numbers:", prime_sum)