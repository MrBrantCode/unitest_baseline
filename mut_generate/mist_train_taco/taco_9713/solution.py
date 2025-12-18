"""
QUESTION:
Imp likes his plush toy a lot.

 [Image] 

Recently, he found a machine that can clone plush toys. Imp knows that if he applies the machine to an original toy, he additionally gets one more original toy and one copy, and if he applies the machine to a copied toy, he gets two additional copies.

Initially, Imp has only one original toy. He wants to know if it is possible to use machine to get exactly x copied toys and y original toys? He can't throw toys away, and he can't apply the machine to a copy if he doesn't currently have any copies.


-----Input-----

The only line contains two integers x and y (0 ≤ x, y ≤ 10^9) — the number of copies and the number of original toys Imp wants to get (including the initial one).


-----Output-----

Print "Yes", if the desired configuration is possible, and "No" otherwise.

You can print each letter in arbitrary case (upper or lower).


-----Examples-----
Input
6 3

Output
Yes

Input
4 2

Output
No

Input
1000 1001

Output
Yes



-----Note-----

In the first example, Imp has to apply the machine twice to original toys and then twice to copies.
"""

def can_get_exact_toys(x: int, y: int) -> str:
    # Imp initially has one original toy, so we need y-1 more original toys
    if y == 0:
        return 'No'
    else:
        y -= 1
    
    # If y is 0 and x is not 0, it's impossible to get any copies without originals
    if y == 0 and x != 0:
        return 'No'
    
    # If the number of original toys needed is greater than the number of copies
    # or if the difference between x and y is odd, it's impossible
    if y > x or (x - y) % 2 != 0:
        return 'No'
    
    # Otherwise, it's possible
    return 'Yes'