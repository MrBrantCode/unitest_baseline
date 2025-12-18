"""
QUESTION:
Write a function named `is_prime_and_fibonacci` that takes an integer `n` as input. The function should first check if `n` is a prime number. If `n` is prime, the function should return "Please enter a non-prime number." If `n` is not prime and `n` is a positive integer greater than 0, the function should generate and print the Fibonacci sequence up to the nth term.
"""

def is_prime_and_fibonacci(n):
    """
    This function checks if the input number is prime, 
    if prime it returns a message, else it generates the Fibonacci sequence up to the nth term.

    Parameters:
    n (int): The number of terms in the Fibonacci sequence.

    Returns:
    str or None: A message if the number is prime, else None.
    """
    
    # check if the number is prime
    def is_prime(num):
        if num > 1:
            for i in range(2, int(num/2)+1):
                if num % i == 0:
                    return False
            return True
        else:
            return False

    # check if the number of terms is valid
    if n <= 0:
        print("Please enter a positive integer.")
    elif is_prime(n):
        return "Please enter a non-prime number."
    else:
        # initialize variables for the first two terms
        first = 0
        second = 1

        # print the first two terms
        print(first)
        print(second)

        # generate the remaining terms
        for i in range(2, n):
            # calculate the next term
            next_term = first + second

            # print the next term
            print(next_term)

            # update the variables for the next iteration
            first = second
            second = next_term