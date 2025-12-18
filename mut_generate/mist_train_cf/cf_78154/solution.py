"""
QUESTION:
Create a function named `rounded_avg_custom_base` that takes three parameters: two distinct positive integers `n` and `m` (where `n <= m`), and an integer `base` within the range of [2, 10]. The function calculates the weighted average of integers between `n` and `m` (inclusive), where the weights correspond to the number of divisors each integer has. The function then rounds this average to the nearest integer and expresses it in the custom base system defined by the `base` parameter. If `n` is greater than `m` or the `base` is outside the allowed range, the function should return -1.
"""

def count_divisors(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

def rounded_avg_custom_base(n, m, base):
    if n > m or base < 2 or base > 10:
        return -1
    total, weight_sum = 0, 0
    for num in range(n, m+1):
        weight = count_divisors(num)
        total += num * weight
        weight_sum += weight
    avg = round(total / weight_sum)
    if base == 2:
        return bin(avg)[2:]
    elif base == 8:
        return oct(avg)[2:]
    elif base == 10:
        return avg
    else:
        converted = ''
        while avg > 0:
            digit = avg % base
            converted = str(digit) + converted
            avg //= base
        return converted