"""
QUESTION:
Create a function `divisors_prime` that takes a list of numbers as input and returns a dictionary. The keys in the dictionary represent the input numbers and the values are tuples. Each tuple contains six elements: 

- a boolean indicating whether the count of divisors is even
- a list of divisors
- the sum of the divisors
- the highest prime number among the divisors (or 'No prime divisors' if no prime divisors exist)
- the lowest common multiple (LCM) of the divisors
- the greatest common divisor (GCD) of the divisors

The function should handle edge scenarios such as negative integers, zero, non-integer inputs, and floating point numbers by ignoring non-integer or negative inputs and returning the closest integer divisors for floating point numbers. The function should be optimized for large numbers and should not use any external libraries or modules.
"""

def divisors_prime(numbers):
    def is_prime(n):
        if n == 1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    
    def gcd(a,b):
        while b > 0:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    def gcd_list(numbers):
        num1 = numbers[0]
        num2 = numbers[1]
        result = gcd(num1,num2)
    
        for i in range(2,len(numbers)):
            result = gcd(result,numbers[i])
        return result
    
    def lcm_list(numbers):
        num1 = numbers[0]
        num2 = numbers[1]
        result = lcm(num1,num2)
    
        for i in range(2,len(numbers)):
            result = lcm(result,numbers[i])
        return result
    
    results = {}
    
    for n in numbers:
        if type(n) != int or n < 1:
            continue 
        divisors = [i for i in range(1, n+1) if n % i == 0]
        sum_of_divisors = sum(divisors)
        prime_divisors = [i for i in divisors if is_prime(i)]
        highest_prime = max(prime_divisors) if prime_divisors else 'No prime divisors'
        gcd_of_divisors = gcd_list(divisors) if len(divisors) > 1 else divisors[0]
        lcm_of_divisors = lcm_list(divisors) if len(divisors) > 1 else divisors[0]
        results[n] = (len(divisors) % 2 == 0, divisors, sum_of_divisors, highest_prime, lcm_of_divisors, gcd_of_divisors)
        
    return results