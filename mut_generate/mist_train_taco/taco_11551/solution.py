"""
QUESTION:
The new PIN is hard to remember. I was told that I shouldn't take notes, but I don't think I can remember them. Therefore, I decided to embed a numerical value in the text and make a note of the PIN. Here, the sum of all the numbers is the PIN.

Create a program that reads the memorandum and outputs the PIN code.



Input

Sentences with embedded positive integers are given over multiple lines. Each line is a character string containing single-byte alphanumeric characters, symbols, and spaces, or a blank line. However, you are guaranteed to enter no more than 80 characters per line and a PIN of 10,000 or less.

Output

The PIN (the sum of positive integers in the text) is output on one line.

Example

Input

Thereare100yenonthetable.Iam17yearsold.
Ishouldgohomeat6pm.


Output

123
"""

import re

def calculate_pin_from_memo(memo: str) -> int:
    """
    Calculate the PIN from the given memorandum text by summing all positive integers embedded in the text.

    Parameters:
    memo (str): The entire memorandum text containing embedded positive integers.

    Returns:
    int: The PIN, which is the sum of all positive integers found in the memo.
    """
    total_sum = 0
    for line in memo.splitlines():
        for number in re.findall(r'\d+', line):
            total_sum += int(number)
    return total_sum