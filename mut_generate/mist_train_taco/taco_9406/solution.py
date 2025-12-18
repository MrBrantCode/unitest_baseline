"""
QUESTION:
You have a positive integer m and a non-negative integer s. Your task is to find the smallest and the largest of the numbers that have length m and sum of digits s. The required numbers should be non-negative integers written in the decimal base without leading zeroes.


-----Input-----

The single line of the input contains a pair of integers m, s (1 ≤ m ≤ 100, 0 ≤ s ≤ 900) — the length and the sum of the digits of the required numbers.


-----Output-----

In the output print the pair of the required non-negative integer numbers — first the minimum possible number, then — the maximum possible number. If no numbers satisfying conditions required exist, print the pair of numbers "-1 -1" (without the quotes).


-----Examples-----
Input
2 15

Output
69 96

Input
3 0

Output
-1 -1
"""

def find_min_max_numbers(m: int, s: int) -> tuple:
    if s > 9 * m:
        return ("-1", "-1")
    elif s == 0:
        if m == 1:
            return ("0", "0")
        else:
            return ("-1", "-1")
    else:
        # Find the smallest number
        min_number = [0] * (m - 1)
        min_number = [1] + min_number
        curr = m - 1
        for _ in range(s - 1):
            min_number[curr] += 1
            if min_number[curr] == 9:
                curr -= 1
        min_number_str = ''.join(map(str, min_number))
        
        # Find the largest number
        max_number = [0] * m
        curr = 0
        for _ in range(s):
            max_number[curr] += 1
            if max_number[curr] == 9:
                curr += 1
        max_number_str = ''.join(map(str, max_number))
        
        return (min_number_str, max_number_str)