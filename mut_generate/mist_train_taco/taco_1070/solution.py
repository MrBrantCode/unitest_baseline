"""
QUESTION:
You have a fraction $\frac{a}{b}$. You need to find the first occurrence of digit c into decimal notation of the fraction after decimal point.


-----Input-----

The first contains three single positive integers a, b, c (1 ≤ a < b ≤ 10^5, 0 ≤ c ≤ 9).


-----Output-----

Print position of the first occurrence of digit c into the fraction. Positions are numbered from 1 after decimal point. It there is no such position, print -1.


-----Examples-----
Input
1 2 0

Output
2
Input
2 3 7

Output
-1


-----Note-----

The fraction in the first example has the following decimal notation: $\frac{1}{2} = 0.500(0)$. The first zero stands on second position.

The fraction in the second example has the following decimal notation: $\frac{2}{3} = 0.666(6)$. There is no digit 7 in decimal notation of the fraction.
"""

def find_first_digit_position(a: int, b: int, c: int) -> int:
    rem1 = -1
    flag = 0
    count = 0
    d = a % b
    
    while d != rem1 and count <= 1000000:
        rem1 = d % b
        count += 1
        d = d * 10
        q = d // b
        if q == c:
            return count
        d = d % b
    
    return -1