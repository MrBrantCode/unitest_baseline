"""
QUESTION:
Implement a function named `modify_string` that takes an input string and returns a new string. The new string should contain characters located at even indices from the original string, followed by characters located at prime indices from the reverse version of the original string in ascending index order. The first character in the string is at index 0.
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def modify_string(input_string):
    even_indices_chars = [input_string[i] for i in range(len(input_string)) if i % 2 == 0]
    reverse_string = input_string[::-1]
    prime_indices_chars = [reverse_string[i] for i in range(len(reverse_string)) if is_prime(i)]
    return ''.join(even_indices_chars + prime_indices_chars)