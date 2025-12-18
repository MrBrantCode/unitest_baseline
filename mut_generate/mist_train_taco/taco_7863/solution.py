"""
QUESTION:
After the fourth season Sherlock and Moriary have realized the whole foolishness of the battle between them and decided to continue their competitions in peaceful game of Credit Cards.

Rules of this game are simple: each player bring his favourite n-digit credit card. Then both players name the digits written on their cards one by one. If two digits are not equal, then the player, whose digit is smaller gets a flick (knock in the forehead usually made with a forefinger) from the other player. For example, if n = 3, Sherlock's card is 123 and Moriarty's card has number 321, first Sherlock names 1 and Moriarty names 3 so Sherlock gets a flick. Then they both digit 2 so no one gets a flick. Finally, Sherlock names 3, while Moriarty names 1 and gets a flick.

Of course, Sherlock will play honestly naming digits one by one in the order they are given, while Moriary, as a true villain, plans to cheat. He is going to name his digits in some other order (however, he is not going to change the overall number of occurences of each digit). For example, in case above Moriarty could name 1, 2, 3 and get no flicks at all, or he can name 2, 3 and 1 to give Sherlock two flicks.

Your goal is to find out the minimum possible number of flicks Moriarty will get (no one likes flicks) and the maximum possible number of flicks Sherlock can get from Moriarty. Note, that these two goals are different and the optimal result may be obtained by using different strategies.


-----Input-----

The first line of the input contains a single integer n (1 ≤ n ≤ 1000) — the number of digits in the cards Sherlock and Moriarty are going to use.

The second line contains n digits — Sherlock's credit card number.

The third line contains n digits — Moriarty's credit card number.


-----Output-----

First print the minimum possible number of flicks Moriarty will get. Then print the maximum possible number of flicks that Sherlock can get from Moriarty.


-----Examples-----
Input
3
123
321

Output
0
2

Input
2
88
00

Output
2
0



-----Note-----

First sample is elaborated in the problem statement. In the second sample, there is no way Moriarty can avoid getting two flicks.
"""

def calculate_flicks(n, sherlock_card, moriarty_card):
    shf = [0] * 10
    mof = [0] * 10
    
    for c in sherlock_card:
        shf[int(c)] += 1
    for c in moriarty_card:
        mof[int(c)] += 1
    
    oshf = shf.copy()
    omof = mof.copy()
    
    sav = 0
    hit = 0
    
    for i in range(9, -1, -1):
        m = min(shf[i], mof[i])
        shf[i] -= m
        mof[i] -= m
        m = min(sav, shf[i])
        sav -= m
        shf[i] -= m
        hit += shf[i]
        sav += mof[i]
        for j in range(10):
            m = min(mof[j], shf[i])
            mof[j] -= m
            shf[i] -= m
    
    min_flicks = hit
    
    shf = oshf
    mof = omof
    
    for i in range(10):
        m = min(mof[i], shf[9])
        mof[i] -= m
        shf[9] -= m
    
    max_flicks = 0
    sav = mof[9]
    
    for i in range(8, -1, -1):
        m = min(shf[i], sav)
        max_flicks += m
        shf[i] -= m
        sav -= m
        sav += mof[i]
    
    return min_flicks, max_flicks