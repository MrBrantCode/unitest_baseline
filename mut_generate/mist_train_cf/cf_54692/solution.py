"""
QUESTION:
Write a function named `compare_one` that takes two parameters `a` and `b` and returns the larger value after converting them to float numbers. If the values are equal, return `None`. The function should handle both numeric and string inputs, replacing any commas with dots before the conversion.
"""

def compare_one(a, b):
    aC = str(a).replace(',', '.') if isinstance(a, str) else str(a)
    bC = str(b).replace(',', '.') if isinstance(b, str) else str(b)

    aN = float(aC)
    bN = float(bC)

    if aN > bN:
        return a
    elif aN < bN:
        return b
    else:
        return None