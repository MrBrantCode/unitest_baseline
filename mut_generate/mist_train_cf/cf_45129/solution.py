"""
QUESTION:
Write a function named `checkPrime(num)` that determines whether a given positive integer `num` is a prime or composite number. The function should print "prime" if `num` is prime and "composite" otherwise. Note that numbers less than 2 are not considered prime.
"""

def checkPrime(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return "composite"
        return "prime"
    else:
        return "composite"