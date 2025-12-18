"""
QUESTION:
Implement the `extract_sequences` function to extract a sequence of digits from the beginning to a defined position in every numeric string of a list. The identified position should be determined by the last digit of each numeric string. The function should handle non-numeric strings and empty lists by ignoring them. Additionally, if the last digit of the numeric string exceeds the string's length, the function should return the full numeric string.
"""

def extract_sequences(numbers):
    result = []
    for num in numbers:
        if not num.isdigit():  # Skip non-numeric strings
            continue
        last_digit = int(num[-1])
        if last_digit > len(num):  # If last digit is larger than string length, return the full sequence
            result.append(num)
        else:  # If not, slice the sequence
            result.append(num[:last_digit])
    return result