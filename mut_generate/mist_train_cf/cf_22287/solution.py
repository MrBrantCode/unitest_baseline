"""
QUESTION:
Create a function called `convert_to_dict` that takes two lists, `num_list` and `char_list`, as input. The function should return a dictionary where the keys are prime numbers from `num_list` and the corresponding values are the characters from `char_list` at the same index. If a prime number appears multiple times in `num_list`, only use its corresponding character once as the value. The returned dictionary should be sorted in descending order based on the keys.
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
    for num, char in zip(num_list, char_list):
        if is_prime(num) and num not in prime_dict:
            prime_dict[num] = char
    return dict(sorted(prime_dict.items(), reverse=True))