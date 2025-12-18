"""
QUESTION:
Write a function named `print_primes(N)` that takes a single argument `N` and prints all prime numbers from 1 to `N`. The function should handle cases where `N` is not a positive integer by printing an error message. Implement this using a while loop and error handling for non-numeric and out-of-range inputs.
"""

def print_primes(N):
    """
    Function to print prime numbers till N
    """
    def is_prime(num):
        """
        Function to check if a number is prime
        """
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
                    break
            else:
                return True
        else:
            return False

    try:
        N = int(N) # Cast to integer in case it was a string
        if N <= 0:
            print("Please enter a number greater than 0.")
        else:
            print("Prime numbers 1 to " + str(N) + " are: ")
            for num in range(1,N+1): # Adding 1 as range is exclusive
                # check for prime
                if is_prime(num):
                    print(num)
    except Exception as e:
        print("Please enter a valid number. Error: ", e)