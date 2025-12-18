"""
QUESTION:
Create a recursive function `print_prime_and_index(lst, idx=0)` that iterates through the given list `lst` and prints the index along with the respective value if the value is a prime number. The function should start checking from the first element (index 0) if no index is provided.
"""

def print_prime_and_index(lst, idx=0):
    def check_prime(n, i=2):
        if n <= 2:
            return True if n == 2 else False
        if n % i == 0:
            return False
        if i * i > n:
            return True
        return check_prime(n, i + 1)

    if idx < len(lst):
        if check_prime(lst[idx]):
            print("Value: {} at Index: {}".format(lst[idx], idx))
        print_prime_and_index(lst, idx + 1)