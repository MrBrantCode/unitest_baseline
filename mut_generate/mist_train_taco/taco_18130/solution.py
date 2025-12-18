"""
QUESTION:
Kitahara Haruki has bought n apples for Touma Kazusa and Ogiso Setsuna. Now he wants to divide all the apples between the friends.

Each apple weights 100 grams or 200 grams. Of course Kitahara Haruki doesn't want to offend any of his friend. Therefore the total weight of the apples given to Touma Kazusa must be equal to the total weight of the apples given to Ogiso Setsuna.

But unfortunately Kitahara Haruki doesn't have a knife right now, so he cannot split any apple into some parts. Please, tell him: is it possible to divide all the apples in a fair way between his friends?


-----Input-----

The first line contains an integer n (1 ≤ n ≤ 100) — the number of apples. The second line contains n integers w_1, w_2, ..., w_{n} (w_{i} = 100 or w_{i} = 200), where w_{i} is the weight of the i-th apple.


-----Output-----

In a single line print "YES" (without the quotes) if it is possible to divide all the apples between his friends. Otherwise print "NO" (without the quotes).


-----Examples-----
Input
3
100 200 100

Output
YES

Input
4
100 100 100 200

Output
NO



-----Note-----

In the first test sample Kitahara Haruki can give the first and the last apple to Ogiso Setsuna and the middle apple to Touma Kazusa.
"""

def can_divide_apples_fairly(n, weights):
    n1 = weights.count(100)
    n2 = weights.count(200)
    
    a = (n2 - n2 // 2) * 200
    b = n2 // 2 * 200
    
    while n1:
        if b <= a:
            b += 100
        else:
            a += 100
        n1 -= 1
    
    return 'YES' if a == b else 'NO'