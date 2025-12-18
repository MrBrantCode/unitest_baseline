"""
QUESTION:
Write a function called `is_prime_cumulative_sum` that takes a list of numerical strings as input. The function should convert these strings into integers, excluding any numbers greater than 20, and then calculate the cumulative sum. If the cumulative sum is a prime number, return the sum; otherwise, return a message indicating that the sum is not a prime number.
"""

def is_prime_cumulative_sum(lst):
    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2): 
            return False
        return all(n % i for i in range(3, int(n**0.5) + 1, 2))
    
    int_list = [int(i) for i in lst if int(i) <= 20]
    cum_sum = sum(int_list)

    return cum_sum if is_prime(cum_sum) else 'Sum is not a prime number.'