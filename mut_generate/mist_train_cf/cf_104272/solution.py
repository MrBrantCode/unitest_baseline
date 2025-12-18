"""
QUESTION:
Write a function `print_hello_world(n)` that prints the string "Hello world!" `n` times if `n` is a positive integer less than 1000. If `n` is not valid, the function should prompt the user to enter a valid input until it receives a positive integer less than 1000. After printing, the function should also return the total number of times "Hello world!" was printed.
"""

def print_hello_world(n):
    count = 0
    while True:
        if n > 0 and n < 1000:
            for _ in range(n):
                print("Hello world!")
                count += 1
            break
        else:
            n = int(input("Enter a valid input: "))

    return count