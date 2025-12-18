"""
QUESTION:
Write a function called `count_nums_plus` that takes an array of integers and strings as input. The function should convert all string entries into integers, ignoring any entries that cannot be converted, and treat the first negative number as a negative. It should then count the number of elements whose cumulative sum is greater than zero and is a multiple of either 4 or 5. The function should return this count.

The function should only consider valid integer conversions and ignore any invalid string entries. It should also correctly handle negative numbers and cumulative sums that meet the specified conditions.
"""

def count_nums_plus(arr):
    """
    A function to count the elements in an array after converting string entries to integers (ignoring invalid entries),
    considering negative numbers, that have a sum greater than zero and are a multiple of 4 or 5.
    """
    result = 0
    sum = 0
    for item in arr:
        try:
            number = int(item)
            sum += number if item != '-' else -number
            if sum > 0 and (sum % 4 == 0 or sum % 5 == 0):
                result += 1
        except ValueError:
            continue
    return result