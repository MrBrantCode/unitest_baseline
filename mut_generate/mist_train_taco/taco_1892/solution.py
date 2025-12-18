"""
QUESTION:
A balance scale tips to the left if L>R, where L is the total weight of the masses on the left pan and R is the total weight of the masses on the right pan. Similarly, it balances if L=R, and tips to the right if L<R.
Takahashi placed a mass of weight A and a mass of weight B on the left pan of a balance scale, and placed a mass of weight C and a mass of weight D on the right pan.
Print Left if the balance scale tips to the left; print Balanced if it balances; print Right if it tips to the right.

-----Constraints-----
 - 1\leq A,B,C,D \leq 10
 - All input values are integers.

-----Input-----
Input is given from Standard Input in the following format:
A B C D

-----Output-----
Print Left if the balance scale tips to the left; print Balanced if it balances; print Right if it tips to the right.

-----Sample Input-----
3 8 7 1

-----Sample Output-----
Left

The total weight of the masses on the left pan is 11, and the total weight of the masses on the right pan is 8. Since 11>8, we should print Left.
"""

def determine_balance_scale_tip(A: int, B: int, C: int, D: int) -> str:
    left_weight = A + B
    right_weight = C + D
    
    if left_weight > right_weight:
        return "Left"
    elif left_weight < right_weight:
        return "Right"
    else:
        return "Balanced"