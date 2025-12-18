"""
QUESTION:
Design an algorithm that takes an integer `n` as input and returns all perfect numbers from 0 to `n` and all amicable pairs up to `n` without repetition. A perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself. An amicable pair is a pair of numbers, each of which is the sum of the proper divisors of the other. The algorithm should be able to handle `n` values up to 10⁴.
"""

def entrance(n):
    """
    This function finds all perfect numbers from 0 to n and all amicable pairs up to n without repetition.

    Args:
        n (int): The upper limit for finding perfect numbers and amicable pairs.

    Returns:
        tuple: A tuple containing two lists. The first list contains all perfect numbers up to n, 
               and the second list contains all amicable pairs up to n.
    """

    def find_divisors(num):
        divisors = [1]
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                if num//i == i:
                    divisors.append(i)
                else:
                    divisors.extend([i, num // i])
        return divisors

    perfect_numbers = [i for i in range(2, n+1) if i == sum(find_divisors(i))]
    amicable_pairs = sorted([sorted([i, sum(find_divisors(i))]) for i in range(2, n+1) if i != sum(find_divisors(i)) and sum(find_divisors(sum(find_divisors(i)))) == i])

    return perfect_numbers, amicable_pairs