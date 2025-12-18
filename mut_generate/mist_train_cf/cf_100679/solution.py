"""
QUESTION:
Calculate the Least Common Multiple (LCM) of numbers from 1 to n using a function named get_lcm(n). The function must account for the prime factors of each number from 1 to n and ensure that the LCM can only contain prime factors less than or equal to n. The function should return the calculated LCM.
"""

def get_lcm(n):
    prime_factors = []
    for i in range(2, n + 1):
        # Find the prime factors of each number from 1 to n
        for j in range(2, i + 1):
            if i % j == 0:
                is_prime = True
                for k in range(2, int(j ** 0.5) + 1):
                    if j % k == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_factors.append(j)
    lcm = 1
    # Loop through the unique prime factors less than or equal to n
    for factor in set(prime_factors):
        max_power = 0
        # Find the highest power of the prime factor that divides any number from 1 to n
        for i in range(1, n + 1):
            power = 0
            while i % factor == 0:
                power += 1
                i //= factor
            if power > max_power:
                max_power = power
        # Multiply the prime factor by its highest power to get the contribution to the LCM
        lcm *= factor ** max_power
    return lcm