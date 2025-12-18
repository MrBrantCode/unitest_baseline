"""
QUESTION:
Write a function named `cumulative_odd_prime_sums` that calculates the cumulative sum of odd numbers within a given range (10 to 50), isolates these odd numbers, and identifies the prime numbers among the cumulative sums. The function should handle potential exceptions and provide informative error messages. Implement this function using functional programming principles where possible.
"""

def cumulative_odd_prime_sums(start, end):
    """
    This function calculates the cumulative sum of odd numbers within a given range,
    isolates these odd numbers, and identifies the prime numbers among the cumulative sums.

    Args:
    start (int): The start of the range.
    end (int): The end of the range.

    Returns:
    list: A list containing the odd numbers, their cumulative sums, and the prime numbers among the cumulative sums.

    Raises:
    Exception: If an error occurs during the calculation.
    """

    def is_prime(n):
        """Helper function that checks if a given number is prime."""
        if n == 1:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    try:
        odd_numbers = [x for x in range(start, end + 1) if x % 2 != 0]
        cumulative_sums = []
        sum = 0
        for num in odd_numbers:
            sum += num
            cumulative_sums.append(sum)

        prime_sums = [x for x in cumulative_sums if is_prime(x)]
        return odd_numbers, cumulative_sums, prime_sums

    except Exception as e:
        raise Exception("An error occurred:", str(e))

# Example usage:
start = 10
end = 50
odd_numbers, cumulative_sums, prime_sums = cumulative_odd_prime_sums(start, end)

print("The odd numbers between {} and {} are:".format(start, end))
print(odd_numbers)
print("The cumulative sum of these numbers are:")
print(cumulative_sums)
print("The prime numbers among the cumulative sums are:")
print(prime_sums)