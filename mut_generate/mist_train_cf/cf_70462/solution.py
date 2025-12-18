"""
QUESTION:
Find the first sequence of binary digits in a larger series where the result of dividing these digits by a divisor equals a given quotient. The sequence of binary digits and the divisor will be provided as inputs to the function `find_binary_sequence`. The function should return the first sequence of binary digits that meets the condition.
"""

def find_binary_sequence(binary_series, divisor, quotient):
    for i in range(len(binary_series)):
        for j in range(i + 1, len(binary_series) + 1):
            if int(binary_series[i:j], 2) / divisor == quotient:
                return binary_series[i:j]
    return None