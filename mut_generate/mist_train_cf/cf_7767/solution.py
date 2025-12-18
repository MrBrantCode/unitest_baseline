"""
QUESTION:
Implement a function `convert_to_dictionary(num_list, char_list)` that takes two lists as input: a list of numbers `num_list` and a list of characters `char_list`. The function should return a dictionary where the numeric values from `num_list` are the keys and the corresponding characters from `char_list` are the values, but only include the numbers that are prime numbers as keys in the dictionary. If a prime number appears multiple times in `num_list`, use the corresponding character in `char_list` only once as the value for that key in the dictionary. The dictionary should be sorted in descending order based on the keys.
"""

def convert_to_dictionary(num_list, char_list):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    result = {}
    for i, num in enumerate(num_list):
        if is_prime(num) and num not in result:
            result[num] = char_list[i]
    return dict(sorted(result.items(), reverse=True))