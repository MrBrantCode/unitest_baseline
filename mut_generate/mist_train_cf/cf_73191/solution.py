"""
QUESTION:
Write a function `custom_divisible(x, y, z, k)` that takes four positive integers `x`, `y`, `z`, and `k` as inputs. The function should return the kth largest even integer in the range [x, y] inclusive that is evenly divisible by z. If k such numbers do not exist within the specified range or the range is invalid, the function should return -1.
"""

def custom_divisible(x, y, z, k):
    """
    This function accepts four positive integers x, y, z and k as inputs. It finds and returns the kth
    largest even integer in the range [x, y] inclusive, which is evenly divisible by z. If k such numbers
    do not exist within the specified range or the range is invalid, the function should return -1.
    """
    if x > y:
        return -1

    divisible_numbers = [num for num in range(x, y + 1) if num % z == 0 and num % 2 == 0]

    if k > len(divisible_numbers):
        return -1
    else:
        divisible_numbers.sort(reverse=True)
        return divisible_numbers[k - 1]