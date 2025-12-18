"""
QUESTION:
Implement the function `steppingNumber` that takes two parameters `low` and `high` of type `int`. The function should initialize a queue with single-digit stepping numbers (0-9) and then iteratively check and add stepping numbers within the range from `low` to `high` to the queue. A stepping number is a number where each digit is one more or one less than the preceding digit. The function should return a dictionary where the keys are the stepping numbers and the values are the sum of the digits in the corresponding stepping numbers.
"""

def steppingNumber(low: int, high: int):
    queue = list(range(10))
    res = []

    while queue:
        num = queue.pop(0)
        if low <= num <= high:
            res.append(num)

        if num == 0 or num > high:
            continue

        lastDigit = num % 10

        if lastDigit > 0:
            nextNum = num * 10 + (lastDigit - 1)
            if nextNum <= high:
                queue.append(nextNum)

        if lastDigit < 9:
            nextNum = num * 10 + (lastDigit + 1)
            if nextNum <= high:
                queue.append(nextNum)

    result_dict = {}
    for i in res:
        list_i = list(map(int, str(i)))
        result_dict[i] = sum(list_i)

    return result_dict