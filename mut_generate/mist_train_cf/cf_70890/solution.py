"""
QUESTION:
Write a function called `find_nums` that takes an integer `n` as input and finds all numbers below `n` that are divisible by 7. The function should also count how many of those numbers are odd. The function must not use any external libraries or the modulus operator (%).
"""

def find_nums(n):
    count = 0
    for i in range(n):
        if i-7*int(i/7) == 0:  # finding multiples of 7 without using modulus
            if i//2*2 != i:  # finding odd numbers without using modulus
                count += 1
    print("Numbers below", n, "that are divisible by 7 and their odd count:")
    for i in range(n):
        if i-7*int(i/7) == 0:  
            print(i)
    print("Count of odd numbers:", count)
    return count