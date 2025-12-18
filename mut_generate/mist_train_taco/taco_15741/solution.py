"""
QUESTION:
Arkady decided to buy roses for his girlfriend.

A flower shop has white, orange and red roses, and the total amount of them is n. Arkady thinks that red roses are not good together with white roses, so he won't buy a bouquet containing both red and white roses. Also, Arkady won't buy a bouquet where all roses have the same color. 

Arkady wants to buy exactly k roses. For each rose in the shop he knows its beauty and color: the beauty of the i-th rose is b_{i}, and its color is c_{i} ('W' for a white rose, 'O' for an orange rose and 'R' for a red rose). 

Compute the maximum possible total beauty of a bouquet of k roses satisfying the constraints above or determine that it is not possible to make such a bouquet.


-----Input-----

The first line contains two integers n and k (1 ≤ k ≤ n ≤ 200 000) — the number of roses in the show and the number of roses Arkady wants to buy.

The second line contains a sequence of integers b_1, b_2, ..., b_{n} (1 ≤ b_{i} ≤ 10 000), where b_{i} equals the beauty of the i-th rose.

The third line contains a string c of length n, consisting of uppercase English letters 'W', 'O' and 'R', where c_{i} denotes the color of the i-th rose: 'W' denotes white, 'O'  — orange, 'R' — red.


-----Output-----

Print the maximum possible total beauty of a bouquet of k roses that satisfies the constraints above. If it is not possible to make a single such bouquet, print -1.


-----Examples-----
Input
5 3
4 3 4 1 6
RROWW

Output
11

Input
5 2
10 20 14 20 11
RRRRR

Output
-1

Input
11 5
5 6 3 2 3 4 7 5 4 5 6
RWOORWORROW

Output
28



-----Note-----

In the first example Arkady wants to buy 3 roses. He can, for example, buy both red roses (their indices are 1 and 2, and their total beauty is 7) and the only orange rose (its index is 3, its beauty is 4). This way the total beauty of the bouquet is 11. 

In the second example Arkady can not buy a bouquet because all roses have the same color.
"""

def max_bouquet_beauty(n, k, b, c):
    if k == 1:
        return -1
    
    roses = sorted([(b[i], c[i]) for i in range(n)], reverse=True)
    
    def calculate_max_beauty(exclude_color):
        total_beauty = 0
        count = 0
        has_white = False
        has_orange = False
        has_red = False
        
        for beauty, color in roses:
            if color != exclude_color:
                total_beauty += beauty
                count += 1
                if color == 'W':
                    has_white = True
                elif color == 'O':
                    has_orange = True
                elif color == 'R':
                    has_red = True
            if count == k:
                break
        
        if count < k:
            return 0
        
        if exclude_color == 'R' and not (has_white and has_orange):
            total_beauty = 0
        elif exclude_color == 'W' and not (has_red and has_orange):
            total_beauty = 0
        
        return total_beauty
    
    max_beauty_excluding_red = calculate_max_beauty('R')
    max_beauty_excluding_white = calculate_max_beauty('W')
    
    if max_beauty_excluding_red or max_beauty_excluding_white:
        return max(max_beauty_excluding_red, max_beauty_excluding_white)
    else:
        return -1