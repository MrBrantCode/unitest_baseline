"""
QUESTION:
Write a function `ArrayAdditionI` that determines whether any combination of the numbers in the given array can be added together to produce the largest number in the array, and returns `true` if such a combination exists and `false` otherwise. The input array will have at least 3 positive integers.
"""

def ArrayAdditionI(arr):
    max_num = max(arr)
    arr.remove(max_num)

    def is_sum_combination(target, numbers):
        if target == 0:
            return True
        if not numbers:
            return False
        num = numbers[0]
        rest = numbers[1:]
        return is_sum_combination(target - num, rest) or is_sum_combination(target, rest)

    return is_sum_combination(max_num, arr)