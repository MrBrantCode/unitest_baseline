"""
QUESTION:
Create a function named `intersperse` that takes three parameters: a list of integers (`numbers`), a single integer (`delimeter`), and another integer (`skip`). The function should return a new list where `delimeter` is inserted between each pair of elements from the `numbers` list, unless the index is equal to `skip - 1` or if `delimeter` is negative and its absolute value equals the index. If `delimeter` is negative, use its absolute value. Do not add `delimeter` after the last number in the `numbers` list.
"""

def intersperse(numbers, delimeter, skip):
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if delimeter >= 0 and i != len(numbers) - 1 and i != skip - 1:
            result.append(delimeter)
        elif delimeter < 0 and -delimeter - 1 != i and i != len(numbers) - 1 and i != skip - 1:
            result.append(abs(delimeter))
    return result