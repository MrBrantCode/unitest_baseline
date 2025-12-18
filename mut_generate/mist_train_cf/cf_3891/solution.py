"""
QUESTION:
Write a function `find_nth_prime(n)` to find the Nth prime number using only a while loop and without using any built-in prime number checking functions or libraries. The solution should have a time complexity of O(N^2) and a space complexity of O(1).
"""

def find_nth_prime(n):
    count = 0
    num = 2
    while count < n:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                count += 1
        num += 1
    return num - 1