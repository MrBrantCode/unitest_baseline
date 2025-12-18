"""
QUESTION:
Construct a function named `count_upper_prime(s)` that calculates the quantity of uppercase vowel characters located precisely at prime digit positions within an entry string `s`. Prime digit positions are based on 1-based indexing and include numbers like 2, 3, 5, 7, 11, and so on. The function should count the occurrences of uppercase vowels ('A', 'E', 'I', 'O', 'U') at these prime digit positions in the string `s`.
"""

def count_upper_prime(s):
    def is_prime(n):
        """ Helper function to check if a number is prime """
        if n == 0 or n == 1:
            return False
        for x in range(2, n//2 + 1):
            if n % x == 0:
                return False
        return True

    """ Count the number of uppercase vowels at prime-numbered positions """
    count = 0
    for i in range(len(s)):
        if is_prime(i + 1):  # +1 for 1-based indexing
            if s[i] in 'AEIOU':  
                count += 1
    return count