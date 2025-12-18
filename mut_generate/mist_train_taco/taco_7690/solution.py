"""
QUESTION:
B: Twins

One twin was angry that it was not well known which of them was the older brother and which was the younger brother.

Create a program that outputs "square1001" when "ani" is entered and "e869120" when "otouto" is entered.

input

You will be given either the string "ani" or "otouto" as input.

output

Please output "e869120" or "square1001" according to the problem statement. Don't forget the last line break.

Input example 1


ani


Output example 1


square1001


Input example 2


otouto


Output example 2


e869120






Example

Input

ani


Output

square1001
"""

def determine_twin_identity(twin_type: str) -> str:
    if twin_type == 'ani':
        return 'square1001'
    elif twin_type == 'otouto':
        return 'e869120'
    else:
        raise ValueError("Invalid input. Expected 'ani' or 'otouto'.")