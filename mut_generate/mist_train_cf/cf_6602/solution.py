"""
QUESTION:
Create a recursive function `print_primes` that prints prime numbers between 0 and 20, excluding 5 and 7. Store these prime numbers in a list and print the list in descending order. Also, calculate the total sum of these prime numbers and check if the total sum is divisible by 3. Use a helper function `is_prime` to check if a number is prime.
"""

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def print_primes(start, end, primes):
    if start > end:
        primes.sort(reverse=True)
        print("Prime numbers in descending order:", primes)
        total_sum = sum(primes)
        print("Total sum of prime numbers:", total_sum)
        if total_sum % 3 == 0:
            print("The total sum is divisible by 3.")
        else:
            print("The total sum is not divisible by 3.")
        return
    if is_prime(start) and start != 5 and start != 7:
        primes.append(start)
    print_primes(start+1, end, primes)