"""
QUESTION:
Write a function named `filter_strings` that takes an array of strings as input and returns a new array containing only the strings from the input array that meet the following conditions:
- The string is entirely composed of digits.
- The string has a length of at least 2.
- The string represents a sequence of consecutive even numbers, where each number is between 10 and 1000 (inclusive).
- The sequence of even numbers is obtained by dividing the string into two-digit numbers from left to right.
- The numbers in the sequence are consecutive in the sense that each number is 2 more than the previous number.
"""

def filter_strings(strings):
    def is_consecutive_even_numbers(s):
        even_numbers = [int(s[i:i+2]) for i in range(0, len(s), 2)]
        return all(10 <= num <= 1000 and num % 2 == 0 for num in even_numbers) and all(even_numbers[i+1] - even_numbers[i] == 2 for i in range(len(even_numbers)-1))

    return [s for s in strings if s.isdigit() and len(s) >= 4 and is_consecutive_even_numbers(s)]