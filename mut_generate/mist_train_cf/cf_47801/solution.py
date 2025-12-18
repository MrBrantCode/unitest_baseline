"""
QUESTION:
Create a function `list_length_and_is_prime` that takes a list as input and prints the length of the list and whether the length is a prime number. The function should handle the case where the input is not a list and print an error message instead.
"""

def list_length_and_is_prime(lst):
    """Print the length of list and check if it's prime"""
    def is_prime(n):
        """Check if the given number is prime"""
        if n <= 1:
            return False
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True

    try: 
        length = len(lst)
        print(f"Length of the list: {length}")
        print(f"Is the number a prime number? {is_prime(length)}")
    except TypeError:
        print("The input is not a list")