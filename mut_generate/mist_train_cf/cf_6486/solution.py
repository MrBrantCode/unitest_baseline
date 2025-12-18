"""
QUESTION:
Write a function `find_second_highest_prime` that finds the second highest prime number in a list of numbers. 

- The function should return the second highest prime number if it exists.
- If the list is empty or does not contain any prime numbers, the function should return an error message indicating the specific issue.
- If the list contains only one prime number, the function should return an error message indicating that there is no second highest prime number.
- The function should have a time complexity of O(n^2), where n is the length of the list.
- The function should have a space complexity of O(1).
- The function should use only basic operations and functions, such as loops and conditional statements, and should not use any built-in functions or libraries for prime number checking.
"""

def find_second_highest_prime(numbers):
    if len(numbers) < 2:
        return "Error: The list should contain at least two numbers."
    
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    highest_prime = float('-inf')
    second_highest_prime = float('-inf')
    has_prime = False
    for number in numbers:
        if is_prime(number):
            has_prime = True
            if number > highest_prime:
                second_highest_prime = highest_prime
                highest_prime = number
            elif number > second_highest_prime:
                second_highest_prime = number
                
    if not has_prime:
        return "Error: The list does not contain any prime numbers."
    elif second_highest_prime == float('-inf'):
        return "Error: There is no second highest prime number in the list."
    else:
        return second_highest_prime