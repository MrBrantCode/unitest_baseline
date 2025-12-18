"""
QUESTION:
AtCoDeer has three cards, one red, one green and one blue.

An integer between 1 and 9 (inclusive) is written on each card: r on the red card, g on the green card and b on the blue card.

We will arrange the cards in the order red, green and blue from left to right, and read them as a three-digit integer.

Is this integer a multiple of 4?  

-----Constraints-----
 - 1 ≤ r, g, b ≤ 9

-----Input-----
Input is given from Standard Input in the following format:
r g b

-----Output-----
If the three-digit integer is a multiple of 4, print YES (case-sensitive); otherwise, print NO.

-----Sample Input-----
4 3 2

-----Sample Output-----
YES

432 is a multiple of 4, and thus YES should be printed.
"""

def is_three_digit_multiple_of_4(r: int, g: int, b: int) -> str:
    # Form the three-digit number from the given digits
    three_digit_number = r * 100 + g * 10 + b
    
    # Check if the three-digit number is a multiple of 4
    if three_digit_number % 4 == 0:
        return "YES"
    else:
        return "NO"