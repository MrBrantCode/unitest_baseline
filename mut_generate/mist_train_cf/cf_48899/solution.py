"""
QUESTION:
Create a function named `remove_and_sort()` that takes a list of tuples as input, where each tuple contains a number and its hexadecimal equivalent. The function should remove any even prime numbers from the list and then return the remaining tuples in descending order by their decimal number. Note that the input list only contains positive integers ranging from 10 to 10,000.
"""

def remove_and_sort(tuples_list):
    def is_odd_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    # remove tuples with even primes.
    tuples_list = [i for i in tuples_list if is_odd_prime(i[0])]
    # sort remaining tuples in descending order.
    tuples_list.sort(key=lambda x: x[0], reverse=True)
    return tuples_list