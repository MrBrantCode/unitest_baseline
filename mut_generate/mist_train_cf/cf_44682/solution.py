"""
QUESTION:
Create a function named `perfect_numbers` that accepts two integers `x` and `n` as inputs, where `x` is the lower limit and `n` is the upper limit. The function should find all perfect numbers within the range from `x` to `n` and determine if each found number is also a Mersenne prime. Note that all perfect numbers discovered so far are even, so the function only needs to check even numbers to avoid unnecessary processing.
"""

def perfect_numbers(x, n):
    def is_perfect(number):
        sum = 1
        i = 2
        while i * i <= number:
            if number % i:
                i += 1
            else:
                if i * (number / i) == number:
                    sum = sum + i + number/i
                else:
                    sum += i
                i += 1
        return sum == number and number!=1

    def is_prime(n):
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True   

    def is_mersenne_prime(p):
        if is_prime(p):
            mp = 2**p - 1
            return is_prime(mp)
        return False

    for i in range(x, n+1):
        if is_perfect(i):
            print("Perfect number: ", i)
            if is_mersenne_prime(i):
               print(i, " is a Mersenne prime")
            else:
               print(i, " is not a Mersenne prime")