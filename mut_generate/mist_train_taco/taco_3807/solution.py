"""
QUESTION:
Everlasting Sa-Ga, a new, hot and very popular role-playing game, is out on October 19, 2008. Fans have been looking forward to a new title of Everlasting Sa-Ga.

Little Jimmy is in trouble. He is a seven-year-old boy, and he obtained the Everlasting Sa-Ga and is attempting to reach the end of the game before his friends. However, he is facing difficulty solving the riddle of the first maze in this game -- Everlasting Sa-Ga is notorious in extremely hard riddles like Neverending Fantasy and Forever Quest.

The riddle is as follows. There are two doors on the last floor of the maze: the door to the treasure repository and the gate to the hell. If he wrongly opens the door to the hell, the game is over and his save data will be deleted. Therefore, he should never open the wrong door.

So now, how can he find the door to the next stage? There is a positive integer given for each door -- it is a great hint to this riddle. The door to the treasure repository has the integer that gives the larger key number. The key number of a positive integer n is the largest prime factor minus the total sum of any other prime factors, where the prime factors are the prime numbers that divide into n without leaving a remainder. Note that each prime factor should be counted only once.

As an example, suppose there are doors with integers 30 and 20 respectively. Since 30 has three prime factors 2, 3 and 5, its key number is 5 - (2 + 3) = 0. Similarly, since 20 has two prime factors 2 and 5, its key number 20 is 5 - 2 = 3. Jimmy therefore should open the door with 20.

Your job is to write a program to help Jimmy by solving this riddle.



Input

The input is a sequence of datasets. Each dataset consists of a line that contains two integers a and b separated by a space (2 ≤ a, b ≤ 106 ). It is guaranteed that key numbers of these integers are always different.

The input is terminated by a line with two zeros. This line is not part of any datasets and thus should not be processed.

Output

For each dataset, print in a line ‘a’ (without quotes) if the door with the integer a is connected to the treasure repository; print ‘b’ otherwise. No extra space or character is allowed.

Example

Input

10 15
30 20
0 0


Output

a
b
"""

import math

def find_treasure_door(a: int, b: int) -> str:
    """
    Determines which door leads to the treasure repository based on the key number calculation.

    Parameters:
    a (int): The integer associated with the first door.
    b (int): The integer associated with the second door.

    Returns:
    str: 'a' if the first door leads to the treasure repository, 'b' otherwise.
    """
    
    def get_prime_factors(n: int) -> list:
        """
        Returns a list of unique prime factors of the given integer n.
        """
        prime_factors = []
        factor = 2
        while n % factor == 0:
            prime_factors.append(factor)
            n //= factor
        factor = 3
        while factor * factor <= n:
            while n % factor == 0:
                prime_factors.append(factor)
                n //= factor
            factor += 2
        if n > 1:
            prime_factors.append(n)
        return list(set(prime_factors))
    
    def calculate_key_number(prime_factors: list) -> int:
        """
        Calculates the key number based on the prime factors.
        """
        prime_factors.sort(reverse=True)
        if len(prime_factors) == 1:
            return prime_factors[0]
        else:
            return prime_factors[0] - sum(prime_factors[1:])
    
    # Get prime factors and calculate key numbers
    prime_factors_a = get_prime_factors(a)
    prime_factors_b = get_prime_factors(b)
    
    key_number_a = calculate_key_number(prime_factors_a)
    key_number_b = calculate_key_number(prime_factors_b)
    
    # Determine which door leads to the treasure repository
    if key_number_a > key_number_b:
        return 'a'
    else:
        return 'b'