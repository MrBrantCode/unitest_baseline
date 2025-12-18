"""
QUESTION:
Write a function `count_nums` that takes an array of integers as input and returns the count of elements whose sum of signed digits exceeds zero and is divisible by 4. The sum of signed digits is calculated by considering the first digit negative if the number is negative.
"""

def count_nums(arr):
    def sum_digits(n):
        sum = 0
        first = True
        for digit in str(n):
            if digit == "-":  # ignore the "-" sign
                continue
            if first:
                if n < 0:
                    sum -= int(digit)
                else:
                    sum += int(digit)
                first = False
            else:
                sum += int(digit)
        return sum

    count = 0
    for num in arr:
        if sum_digits(num) > 0 and sum_digits(num) % 4 == 0:
            count += 1

    return count