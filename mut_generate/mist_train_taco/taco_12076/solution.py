"""
QUESTION:
User ainta loves to play with cards. He has a cards containing letter "o" and b cards containing letter "x". He arranges the cards in a row, and calculates the score of the deck by the formula below.

  1. At first, the score is 0. 
  2. For each block of contiguous "o"s with length x the score increases by x2. 
  3. For each block of contiguous "x"s with length y the score decreases by y2. 



For example, if a = 6, b = 3 and ainta have arranged the cards in the order, that is described by string "ooxoooxxo", the score of the deck equals 22 - 12 + 32 - 22 + 12 = 9. That is because the deck has 5 blocks in total: "oo", "x", "ooo", "xx", "o".

User ainta likes big numbers, so he wants to maximize the score with the given cards. Help ainta make the score as big as possible. Note, that he has to arrange all his cards.

Input

The first line contains two space-separated integers a and b (0 ≤ a, b ≤ 105; a + b ≥ 1) — the number of "o" cards and the number of "x" cards.

Output

In the first line print a single integer v — the maximum score that ainta can obtain.

In the second line print a + b characters describing the deck. If the k-th card of the deck contains "o", the k-th character must be "o". If the k-th card of the deck contains "x", the k-th character must be "x". The number of "o" characters must be equal to a, and the number of "x " characters must be equal to b. If there are many ways to maximize v, print any.

Please, do not write the %lld specifier to read or write 64-bit integers in С++. It is preferred to use the cin, cout streams or the %I64d specifier.

Examples

Input

2 3


Output

-1
xoxox


Input

4 0


Output

16
oooo

Input

0 4


Output

-16
xxxx
"""

def maximize_card_score(a, b):
    def sx(p):
        return (a - p + 1) ** 2 + p - 1
    
    def sy(q):
        return b % q * (1 + b // q) ** 2 + (b // q) ** 2 * (q - b % q)
    
    if a == 0:
        return -b ** 2, b * 'x'
    elif b <= 1:
        return a ** 2 - b ** 2, a * 'o' + b * 'x'
    else:
        n = min(a, b)
        res = -(a + b) ** 2
        res_p = res_q = 0
        
        for p in range(1, n + 1):
            for q in range(p - 1, p + 2):
                if 1 <= q <= b:
                    pos = sx(p)
                    neg = sy(q)
                    if res < pos - neg:
                        res = pos - neg
                        res_p = p
                        res_q = q
        
        max_score = res
        deck_arrangement = ''
        
        if res_p >= res_q:
            for i in range(res_p):
                wl = 1 if i > 0 else a - (res_p - 1)
                deck_arrangement += wl * 'o'
                ll = b // res_q + 1 if i < b % res_q else b // res_q
                if i < res_q:
                    deck_arrangement += ll * 'x'
        else:
            for i in range(res_q):
                ll = b // res_q + 1 if i < b % res_q else b // res_q
                deck_arrangement += ll * 'x'
                wl = 1 if i > 0 else a - (res_p - 1)
                if i < res_p:
                    deck_arrangement += wl * 'o'
        
        return max_score, deck_arrangement