"""
QUESTION:
Write a function called `second_smallest` that takes an array of numbers as input and returns the second lowest numerical element within the array. The function should not use built-in methods or libraries and should handle potential errors such as non-integer inputs within the array. If the array has less than two unique integers, the function should return `None`. If the array contains non-integer values, the function should print an error message for each non-integer value and exclude it from the comparison.
"""

def second_smallest(numbers):
    count = 0
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if not isinstance(x, int):
            print("Error: Non-integer value", x, "found in the list.")
            continue
        count += 1
        if x < m1:
            m1, m2 = x, m1
        elif x < m2 and x != m1:
            m2 = x
    return m2 if count > 1 else None