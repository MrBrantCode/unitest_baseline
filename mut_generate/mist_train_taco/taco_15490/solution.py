"""
QUESTION:
Problem statement

AOR Ika-chan is in a bad mood lately. Apparently, I don't like the ratio of the number of followers to the number of followers of "Ikatta". Currently, AOR Ika-chan has $ A $ followers, $ B $ followers, and a ratio of $ A: B $.

Therefore, AOR Ika decided to increase or decrease the number of followers so that the ratio of the number of followers to the number of followers would be an integer ratio that she liked. The integer ratio I like is a ratio that can be expressed so that both values ​​included in the ratio are integers of $ 1 $ or more and $ N $ or less.

However, AOR Ika doesn't want to change the number of followers as much as possible, so I want to make the absolute value of the difference from before the change as small as possible. Create a program that asks at least how many followers you need to change to make AOR Ika feel good.

Input constraints

$ 1 \ le A, \ B \ le 10 ^ {12} $
$ 1 \ leq N \ leq 100 $

sample

Sample input 1


19 30 3


Sample output 1


1


Sample input 2


3 7 7


Sample output 2


0


Sample input 3


3 7 1


Sample output 3


Four


Sample input 4


102 30 3


Sample output 4


12


By reducing the number of followers by $ 12 $, it becomes $ 90: 30 \ (= 3: 1) $, and the higher ratio number is $ 3 $ or less.
At this time, the amount of change is $ 12 $.

Sample input 5


3 4 2


Sample output 5


1


If you unfollow one person, it will be $ 2: 4 \ (= 1: 2) $, and if you follow it, it will be $ 4: 4 \ (= 1: 1) $. In both cases, the absolute value of increase / decrease is $ 1 $, which is the answer.

Sample input 6


1 100 2


Sample output 6


49


Please note that at least $ 1 $ people must be following.



input

$ A \ B \ N $

output

Output the minimum absolute value of the amount of change in $ A $, which can be an integer ratio you like.

Example

Input

19 30 3


Output

1
"""

def find_min_follower_change(A, B, N):
    score = abs(A - B)
    for x in range(1, N + 1):
        for y in range(1, N + 1):
            if B * x % y == 0:
                new_a = B * x // y
                score = min(score, abs(A - new_a))
    return score