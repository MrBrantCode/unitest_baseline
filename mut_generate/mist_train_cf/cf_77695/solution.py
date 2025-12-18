"""
QUESTION:
Create a function `add_large_numbers` that takes two lists of integers, `number1` and `number2`, each representing a large number in reverse order where each element is a single digit. The function should perform addition of these two large numbers and return the result as a list of digits in reverse order. The function should handle cases where the input lists have different lengths and any carry-over from the addition of digits. The time complexity of the solution should be O(n), where n is the length of the longer input list.
"""

def add_large_numbers(number1, number2):
    # If the lengths of the numbers are different, pad the shorter one with zeros
    length_diff = len(number1) - len(number2)
    if length_diff > 0:
        number2 += [0] * length_diff
    elif length_diff < 0:
        number1 += [0] * -length_diff

    result = [0] * len(number1)
    carry = 0
    for i in range(len(number1)):
        temp = number1[i] + number2[i] + carry
        result[i] = temp % 10
        carry = temp // 10

    # If there is a carry after the last step, add it to result
    if carry != 0:
        result.append(carry)

    return result