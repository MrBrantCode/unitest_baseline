"""
QUESTION:
Bizon the Champion is called the Champion for a reason. 

Bizon the Champion has recently got a present — a new glass cupboard with n shelves and he decided to put all his presents there. All the presents can be divided into two types: medals and cups. Bizon the Champion has a_1 first prize cups, a_2 second prize cups and a_3 third prize cups. Besides, he has b_1 first prize medals, b_2 second prize medals and b_3 third prize medals. 

Naturally, the rewards in the cupboard must look good, that's why Bizon the Champion decided to follow the rules:  any shelf cannot contain both cups and medals at the same time;  no shelf can contain more than five cups;  no shelf can have more than ten medals. 

Help Bizon the Champion find out if we can put all the rewards so that all the conditions are fulfilled.


-----Input-----

The first line contains integers a_1, a_2 and a_3 (0 ≤ a_1, a_2, a_3 ≤ 100). The second line contains integers b_1, b_2 and b_3 (0 ≤ b_1, b_2, b_3 ≤ 100). The third line contains integer n (1 ≤ n ≤ 100).

The numbers in the lines are separated by single spaces.


-----Output-----

Print "YES" (without the quotes) if all the rewards can be put on the shelves in the described manner. Otherwise, print "NO" (without the quotes).


-----Examples-----
Input
1 1 1
1 1 1
4

Output
YES

Input
1 1 3
2 3 4
2

Output
YES

Input
1 0 0
1 0 0
1

Output
NO
"""

def can_place_rewards(a1, a2, a3, b1, b2, b3, n):
    def required_shelves(total, max_per_shelf):
        if total == 0:
            return 0
        elif total / max_per_shelf <= 1:
            return 1
        elif total % max_per_shelf == 0:
            return int(total / max_per_shelf)
        else:
            return int(total / max_per_shelf) + 1
    
    sum_cups = a1 + a2 + a3
    sum_medals = b1 + b2 + b3
    
    required_shelves_cups = required_shelves(sum_cups, 5)
    required_shelves_medals = required_shelves(sum_medals, 10)
    
    if required_shelves_cups + required_shelves_medals <= n:
        return "YES"
    else:
        return "NO"