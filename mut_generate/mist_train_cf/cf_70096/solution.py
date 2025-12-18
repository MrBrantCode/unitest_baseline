"""
QUESTION:
Write a function `getMaxTriples` that takes an integer `n` as input, calculates the number of triples `(i, j, k)` from the array `a` of length `n` where `a[i] = i * i - i + 1 + i % 3`, and `(a[i] * a[j]) % a[k]` is a multiple of `n`. The function should return the count of such triples. The function should be efficient enough to handle large values of `n`.
"""

def get_max_triples(n):
    """
    Calculate the number of triples (i, j, k) from the array 'a' of length 'n' 
    where a[i] = i * i - i + 1 + i % 3, and (a[i] * a[j]) % a[k] is a multiple of 'n'.
    
    Parameters:
    n (int): The length of the array 'a'.
    
    Returns:
    int: The count of triples satisfying the given condition.
    """
    # Create an array 'a' of length 'n' with elements as per the given formula
    a = [((i+1) * (i+1) - (i+1) + 1) + ((i+1) % 3) for i in range(n)]

    triple_count = 0  # Initialize variable to count triples

    # For all possible combinations of three items (a[i], a[j], a[k])
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Calculate the modulus of the product of any two elements by the third
                product = (a[i] * a[j]) % a[k]
                # Check if the result is a multiple of n
                if product % n == 0:
                    triple_count += 1  # Increment the counter if true

    return triple_count  # Return the number of desired triples