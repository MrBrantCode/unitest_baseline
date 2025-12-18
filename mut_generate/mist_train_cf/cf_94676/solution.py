"""
QUESTION:
Create a function `classify_integer(num)` that takes an integer `num` as input and returns a string indicating its classification. The function should return "positive" if `num` is a positive even number, "negative" if `num` is a negative odd number, "zero" if `num` is 0, and "unknown" if `num` is not an integer or falls outside the range -1000 to 1000 (inclusive).
"""

def classify_integer(num):
    if not isinstance(num, int):
        return "unknown"
    elif num == 0:
        return "zero"
    elif num < -1000 or num > 1000:
        return "unknown"
    elif num > 0 and num % 2 == 0:
        return "positive"
    elif num < 0 and num % 2 != 0:
        return "negative"
    else:
        return "unknown"