"""
QUESTION:
Write a function `calculate_total` that takes three arrays `a`, `b`, and `c` as input, each representing a three-digit number where the first element is the units, the second element is the tens, and the third element is the hundreds. The function should return the combined total of these three values increased by five units, in the same array format.
"""

def calculate_total(a, b, c):
    def array_to_num(arr):
        return arr[0] + arr[1]*10 + arr[2]*100

    def num_to_array(num):
        return [num % 10, (num // 10) % 10, num // 100]

    total = array_to_num(a) + array_to_num(b) + array_to_num(c) + 5
    return num_to_array(total)