"""
QUESTION:
Develop a function `generate_factors(n)` that takes a large integer `n` (up to 10^12) as input and returns its prime factors efficiently. The function should manage memory effectively and run within a reasonable time for large inputs. The input number `n` will be at least 2, and the function should handle both small and large inputs.
"""

def generate_factors(n):
    factors = []

    # divide number by 2 until it's impossible
    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    # divide number by odd numbers from 3 to square root of n
    for i in range(3, int(n**0.5)+1, 2):
        while n % i== 0:
            factors.append(int(i))
            n = n / i
        
    if n > 2:
        factors.append(int(n))

    return factors