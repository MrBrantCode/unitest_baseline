"""
QUESTION:
Write a function `compare_objects(obj1, obj2)` that compares two objects with attributes "name", "age", and "address". The function should return an integer indicating their order. 

The comparison should be based on the following rules:

- If one object's age is a prime number and the other's is not, the object with the prime age is considered larger.
- If both ages are prime numbers, the objects should be compared based on their addresses.
- If neither age is a prime number or both are prime numbers and have the same address, the objects should be compared based on their ages.
- If the ages are equal, the objects should be compared based on their names.
- If the names are equal, the objects should be compared based on their addresses.

The function should return 0 if the objects are equal, a positive number if obj1 is larger, and a negative number if obj2 is larger.
"""

def is_prime(n):
    # Check if a number is prime
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def compare_addresses(obj1, obj2):
    # Compare addresses
    if obj1["address"] > obj2["address"]:
        return 1
    elif obj1["address"] < obj2["address"]:
        return -1
    return 0

def compare_objects(obj1, obj2):
    # Check if the ages of both objects are prime numbers
    obj1_prime = is_prime(obj1["age"])
    obj2_prime = is_prime(obj2["age"])
    
    if obj1_prime and obj2_prime:
        # If both ages are prime numbers, compare their addresses
        return compare_addresses(obj1, obj2)
    elif obj1_prime:
        # If only obj1's age is prime, consider obj1 to be larger
        return 1
    elif obj2_prime:
        # If only obj2's age is prime, consider obj2 to be larger
        return -1
    
    # Compare ages
    if obj1["age"] > obj2["age"]:
        return 1
    elif obj1["age"] < obj2["age"]:
        return -1
    
    # If ages are the same, compare names
    if obj1["name"] > obj2["name"]:
        return 1
    elif obj1["name"] < obj2["name"]:
        return -1
    
    # If names are the same, compare addresses
    return compare_addresses(obj1, obj2)