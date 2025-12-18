"""
QUESTION:
Implement a function `three_way_partition(arr)` that takes an array of integers as input and returns a new list containing unique elements from the original array, sorted in descending order with all odd numbers first, even numbers in the middle, and prime numbers last. The function should not use any built-in sorting functions or libraries.
"""

def three_way_partition(arr):
    odd_list = []
    even_list = []
    prime_list = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for num in arr:
        if num % 2 != 0 and num not in odd_list:
            odd_list.append(num)
        elif num % 2 == 0 and num not in even_list and not is_prime(num):
            even_list.append(num)
        elif is_prime(num) and num not in prime_list:
            prime_list.append(num)
    
    odd_list.sort(reverse=True)
    even_list.sort(reverse=True)
    prime_list.sort(reverse=True)
    
    return odd_list + even_list + prime_list