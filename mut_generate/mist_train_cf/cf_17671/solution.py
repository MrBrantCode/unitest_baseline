"""
QUESTION:
Create a function named `prime_multiplication_table` that generates a 10x10 multiplication table containing only prime numbers, formats it in a visually appealing way, and calculates the sum of all the prime numbers in the table. The table should maintain its original 10x10 shape with empty spaces for non-prime numbers.
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_multiplication_table():
    table = [[0] * 10 for _ in range(10)]
    primes = []
    prime_sum = 0

    for i in range(10):
        for j in range(10):
            num = (i+1) * (j+1)
            if is_prime(num):
                table[i][j] = num
                primes.append(num)
                prime_sum += num

    # Format and display the table
    for row in table:
        for num in row:
            if num != 0:
                print(f'{num:4}', end=' ')
            else:
                print('    ', end=' ')
        print()

    print("\nSum of prime numbers in the table:", prime_sum)

    return prime_sum