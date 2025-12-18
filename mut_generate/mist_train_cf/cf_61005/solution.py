"""
QUESTION:
Develop a function `find_max_divisors(numbers)` that takes a collection of unique integers. The function should return the number with the highest quantity of divisors. If multiple numbers have the same maximum divisor count, the function should return the smallest number amongst them.
"""

def find_max_divisors(numbers):
    def num_divisors(n):
        return sum(1 for i in range(1, n + 1) if n % i == 0)

    max_cnt = -1
    res = None
    for num in numbers:
        cnt = num_divisors(num)
        if cnt > max_cnt or (cnt == max_cnt and num < res):
            max_cnt, res = cnt, num
    return res