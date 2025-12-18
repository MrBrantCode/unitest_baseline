"""
QUESTION:
Implement a function named `multiply` that takes two strings representing integers, each having at most 100 digits, as input and returns their product as a string without using any built-in multiplication or division operators. The function should have a time complexity of O(n), where n is the number of digits in the larger integer.
"""

def multiply(num1, num2):
    num1 = [int(digit) for digit in num1]
    num2 = [int(digit) for digit in num2]

    num1.reverse()
    num2.reverse()

    result = [0] * (len(num1) + len(num2))

    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j] += num1[i] * num2[j]
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    result.reverse()

    result = ''.join(map(str, result))

    return result