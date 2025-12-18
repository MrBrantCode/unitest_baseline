"""
QUESTION:
Create a function called `odd_sum_prime_index_elements(x)` that takes a list of elements as input. The function should return a sorted list of unique elements in ascending order, where each element's digits sum to an odd number and its original index in the input list is a prime number. If the input is not a list or contains non-numeric elements, the function should return "Input is not a list" or "Non-numeric elements found" respectively.
"""

def odd_sum_prime_index_elements(x):
    if not isinstance(x, list):
        return "Input is not a list"
    if not all(isinstance(i, (int, float)) for i in x):
        return "Non-numeric elements found"

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_index_elements = [x[i] for i in range(len(x)) if is_prime(i)]
    return sorted(list(dict.fromkeys([i for i in prime_index_elements if sum(int(digit) for digit in str(int(i))) % 2 != 0])))