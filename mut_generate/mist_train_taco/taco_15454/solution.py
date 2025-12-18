"""
QUESTION:
Do you remember how Kai constructed the word "eternity" using pieces of ice as components?

Little Sheldon plays with pieces of ice, each piece has exactly one digit between 0 and 9. He wants to construct his favourite number t. He realized that digits 6 and 9 are very similar, so he can rotate piece of ice with 6 to use as 9 (and vice versa). Similary, 2 and 5 work the same. There is no other pair of digits with similar effect. He called this effect "Digital Mimicry".

Sheldon favourite number is t. He wants to have as many instances of t as possible. How many instances he can construct using the given sequence of ice pieces. He can use any piece at most once. 


-----Input-----

The first line contains integer t (1 ≤ t ≤ 10000). The second line contains the sequence of digits on the pieces. The length of line is equal to the number of pieces and between 1 and 200, inclusive. It contains digits between 0 and 9.


-----Output-----

Print the required number of instances.


-----Examples-----
Input
42
23454

Output
2

Input
169
12118999

Output
1



-----Note-----

This problem contains very weak pretests.
"""

def count_instances_of_favorite_number(t: str, s: str) -> int:
    s = list(s)
    copies = 0
    
    # Count special cases for 6/9 and 2/5
    x_69 = t.count('6') + t.count('9')
    y_69 = s.count('6') + s.count('9')
    a_25 = t.count('2') + t.count('5')
    b_25 = s.count('2') + s.count('5')
    
    if x_69 == 0 and a_25 == 0:
        copies = 100
    elif x_69 == 0:
        copies = b_25 // a_25
    elif a_25 == 0:
        copies = y_69 // x_69
    else:
        copies = min(y_69 // x_69, b_25 // a_25)
    
    # Count other digits
    for j in range(0, 10):
        i = str(j)
        if i in ['6', '9', '2', '5']:
            continue
        x = t.count(i)
        if x == 0:
            continue
        y = s.count(i)
        copies = min(copies, y // x)
    
    return copies