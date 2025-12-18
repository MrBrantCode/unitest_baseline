"""
QUESTION:
Generate a list of all prime numbers between two given numbers `start_num` and `end_num` (inclusive). Implement a function `generate_prime_list(start_num, end_num)` that returns this list. The function should not take any inputs other than `start_num` and `end_num`.
"""

import math

def generate_prime_list(start_num, end_num):
    prime_list = []
    for num in range(start_num, end_num + 1):
        if num < 2:
            continue
        elif num == 2:
            prime_list.append(num)
        else:
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list