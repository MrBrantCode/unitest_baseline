"""
QUESTION:
Write a function called `delete_largest_prime` that takes a list of positive integers as input and returns the modified list after deleting all occurrences of the largest prime number in the list.
"""

def delete_largest_prime(my_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    largest_prime = 0
    for num in my_list:
        if is_prime(num) and num > largest_prime:
            largest_prime = num
    
    modified_list = [num for num in my_list if num != largest_prime]
    return modified_list