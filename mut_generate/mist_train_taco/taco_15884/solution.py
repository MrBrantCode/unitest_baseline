"""
QUESTION:
Problem

One day, mo3tthi and tubuann decided to play a game with magic pockets and biscuits.
Now there are $ K $ pockets, numbered $ 1,2, \ ldots, K $.
The capacity of the $ i $ th pocket is $ M_i $, which initially contains $ N_i $ biscuits.
mo3tthi and tubuann start with mo3tthi and perform the following series of operations alternately.


* Choose one pocket.
* Perform one of the following operations only once. However, if the number of biscuits in the pocket selected as a result of the operation exceeds the capacity of the pocket, the operation cannot be performed.
* Stroking the selected pocket. Magical power increases the number of biscuits in your chosen pocket by $ 1 $.
* Hit the selected pocket. The number of biscuits in the pocket chosen by magical power is doubled by $ 2 $.



The game ends when you can't operate it, the person who can't operate loses, and the person who doesn't can win.
You, a friend of mo3tthi, were asked by mo3tthi in advance if you could decide if you could win this game.
For mo3tthi, make a program to determine if mo3tthi can definitely win this game.

Constraints

The input satisfies the following conditions.

* $ 1 \ leq K \ leq 10 ^ 5 $
* $ 1 \ leq N_i \ leq M_i \ leq 10 ^ {18} $
* All inputs are integers

Input

The input is given in the following format.


$ K $
$ N_1 $ $ M_1 $
$ \ vdots $
$ N_K $ $ M_K $


Output

When mo3tthi acts optimally, "mo3tthi" is output on one line if he can win, and "tubuann" is output otherwise.

Examples

Input

1
2 4


Output

mo3tthi


Input

2
2 3
3 8


Output

tubuann


Input

10
2 8
5 9
7 20
8 41
23 48
90 112
4 5
7 7
2344 8923
1 29


Output

mo3tthi
"""

def determine_winner(K, pockets):
    ans = 0
    for N, M in pockets:
        grundy0 = {0}
        grundy1 = {1}
        m = M
        while m // 2 >= N:
            if (m + 1) // 2 % 2:
                grundy_l = grundy0
            else:
                grundy_l = grundy1
            m, r = divmod(m, 2)
            if r == 0:
                gr0 = grundy0
                grundy0 = {min({0, 1, 2} - grundy0 - grundy_l)}
                grundy1 = {0, 1, 2} - gr0 - grundy0
            else:
                grundy0 = {min({0, 1, 2} - grundy1 - grundy_l)}
                grundy1 = {0, 1, 2} - grundy1 - grundy0
        grundy = grundy1 if (m - N) % 2 else grundy0
        ans ^= grundy.pop()
    return 'tubuann' if ans == 0 else 'mo3tthi'