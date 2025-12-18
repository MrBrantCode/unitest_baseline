"""
QUESTION:
The new "Die Hard" movie has just been released! There are n people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 ruble bill. A "Die Hard" ticket costs 25 rubles. Can the booking clerk sell a ticket to each person and give the change if he initially has no money and sells the tickets strictly in the order people follow in the line?


-----Input-----

The first line contains integer n (1 ≤ n ≤ 10^5) — the number of people in the line. The next line contains n integers, each of them equals 25, 50 or 100 — the values of the bills the people have. The numbers are given in the order from the beginning of the line (at the box office) to the end of the line.


-----Output-----

Print "YES" (without the quotes) if the booking clerk can sell a ticket to each person and give the change. Otherwise print "NO".


-----Examples-----
Input
4
25 25 50 50

Output
YES

Input
2
25 100

Output
NO

Input
4
50 50 25 25

Output
NO
"""

def can_sell_tickets(n, bills):
    counter = [0, 0, 0]  # [25 ruble bills, 50 ruble bills, 100 ruble bills]
    
    for bill in bills:
        if bill == 25:
            counter[0] += 1
        elif bill == 50:
            if counter[0] < 1:
                return "NO"
            counter[0] -= 1
            counter[1] += 1
        elif bill == 100:
            if counter[1] > 0 and counter[0] > 0:
                counter[1] -= 1
                counter[0] -= 1
            elif counter[0] >= 3:
                counter[0] -= 3
            else:
                return "NO"
    
    return "YES"