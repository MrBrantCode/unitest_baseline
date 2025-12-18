"""
QUESTION:
Create a function `convert_to_dict` that takes two lists as input, `num_list` and `char_list`, where `num_list` contains numbers and `char_list` contains characters. The function should return a dictionary where the prime numbers from `num_list` are the keys and the corresponding characters from `char_list` are the values, with the following restrictions: 
- Each prime number key should only be included once, even if it appears multiple times in `num_list`.
- The dictionary should be sorted in descending order based on the keys.
- The index of the character in `char_list` corresponds to the index of the prime number in `num_list`.
"""

def convert_to_dict(num_list, char_list):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    prime_dict = {}
    for num in num_list:
        if is_prime(num) and num not in prime_dict:
            prime_dict[num] = char_list[num_list.index(num)]
    prime_dict = dict(sorted(prime_dict.items(), reverse=True))
    return prime_dict