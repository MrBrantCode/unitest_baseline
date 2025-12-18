"""
QUESTION:
Write a function `select_prime_records` that takes a table as input where each row represents a record with 'ID', 'Name', and 'Address' fields. Return all records where the 'ID' is a prime number greater than 5. Assume the table is represented as a list of dictionaries in Python, where each dictionary has 'ID', 'Name', and 'Address' keys.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def select_prime_records(table):
    return [record for record in table if is_prime(record['ID']) and record['ID'] > 5]