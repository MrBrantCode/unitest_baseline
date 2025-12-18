"""
QUESTION:
Create a function `count_embedded_primes(num)` that takes a positive integer `num` as input and returns the number of prime numbers embedded within it. A prime number is considered embedded if it can be formed by a contiguous substring of the digits of `num`. The function should count each embedded prime number exactly once, regardless of its position or length within `num`.
"""

def count_embedded_primes(num):
    def is_prime(n):
        """check if integer n is a prime"""
        # make sure n is a positive integer
        n = abs(int(n))
        # 0 and 1 are not primes
        if n < 2:
            return False
        # 2 is the only even prime number
        if n == 2: 
            return True    
        # all other even numbers are not primes
        if not n & 1: 
            return False
        # range starts with 3 and only needs to go up the square root of n for all odd numbers
        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                return False
        return True

    num_str = str(num)
    len_num = len(num_str)
    count = set()
    
    for i in range(len_num):
        for j in range(i+1, len_num+1):
            sub_num = int(num_str[i:j])
            if(is_prime(sub_num)):
                count.add(sub_num)
                
    return len(count)