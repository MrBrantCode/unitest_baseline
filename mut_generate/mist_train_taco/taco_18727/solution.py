"""
QUESTION:
Sereja has two integers — A and B — in 7-ary system. He wants to calculate the number C, such that B * C = A. It is guaranteed that B is a divisor of A.

Please, help Sereja calculate the number C modulo 7L.

-----Input-----

First line of input contains an integer T — the number of test cases. T tests follow.

For each test case, the first line contains the integer A, and the second line contains the integer B, and the third line contains the integer L. A and B are given in 7-ary system.

-----Output-----
Output the answer in 7-ary system.

-----Constraints-----
- 1 ≤ T ≤ 10
- A and B are both positive integers.
- Length of A is a positive integer and doesn't exceed 106.
- L and length of B are positive integers and do not exceed 10000.

-----Subtasks-----
- Sub task #1 (20 points): Length of A is a positive integer and doesn't exceed 20.
- Sub task #2 (30 points): Length of A is a positive integer and doesn't exceed 2000.
- Sub task #3 (50 points): Original constraints.

-----Example-----
Input:3
21
5
10
202
13
1
202
13
2

Output:3
3
13
"""

def calculate_c_in_septary(A: str, B: str, L: int) -> str:
    def septary_to_decimal(num_str: str) -> int:
        decimal_value = 0
        power = 0
        for digit in reversed(num_str):
            decimal_value += int(digit) * (7 ** power)
            power += 1
        return decimal_value

    def decimal_to_septary(num: int, length: int) -> str:
        septary_value = ""
        while num > 0:
            septary_value = str(num % 7) + septary_value
            num //= 7
        return septary_value.zfill(length)

    # Convert A and B from septary to decimal
    A_decimal = septary_to_decimal(A)
    B_decimal = septary_to_decimal(B)

    # Calculate C in decimal
    C_decimal = A_decimal // B_decimal

    # Convert C from decimal to septary with length L
    C_septary = decimal_to_septary(C_decimal, L)

    return C_septary