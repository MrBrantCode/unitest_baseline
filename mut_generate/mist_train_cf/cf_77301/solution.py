"""
QUESTION:
Create a function named get_max_triples that takes a positive integer n as input. The function should generate an array 'a' of length 'n' with elements a[i] = (i * i - i + 1) + (i % 3) for each i (1 ≤ i ≤ n). It should then calculate the modulus of the product of any two elements by the third for all potential combinations of three items (a[i], a[j], a[k]) where i < j < k, and count the number of instances where the resulting outcome is a multiple of n. The function should return this count.
"""

def get_max_triples(n):
    # Create an array 'a' of length 'n' with elements as per the given formula
    a = [(i * i - i + 1) + (i % 3) for i in range(1, n + 1)]
    triple_count = 0  # Initialize variable to count triples

    #For all possible combinations of three items (a[i], a[j], a[k])
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Calculate the modulus of the product of any two elements by the third
                product = (a[i] * a[j]) % a[k]
                # Check if the result is a multiple of n
                if product % n == 0:
                    triple_count += 1  # Increment the counter if true

    return triple_count  # Return the number of desired triples