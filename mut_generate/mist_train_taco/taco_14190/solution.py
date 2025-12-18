"""
QUESTION:
You have N bamboos. The lengths (in centimeters) of these are l_1, l_2, ..., l_N, respectively.
Your objective is to use some of these bamboos (possibly all) to obtain three bamboos of length A, B, C. For that, you can use the following three kinds of magics any number:
 - Extension Magic: Consumes 1 MP (magic point). Choose one bamboo and increase its length by 1.
 - Shortening Magic: Consumes 1 MP. Choose one bamboo of length at least 2 and decrease its length by 1.
 - Composition Magic: Consumes 10 MP. Choose two bamboos and combine them into one bamboo. The length of this new bamboo is equal to the sum of the lengths of the two bamboos combined. (Afterwards, further magics can be used on this bamboo.)
At least how much MP is needed to achieve the objective?

-----Constraints-----
 - 3 \leq N \leq 8
 - 1 \leq C < B < A \leq 1000
 - 1 \leq l_i \leq 1000
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
N A B C
l_1
l_2
:
l_N

-----Output-----
Print the minimum amount of MP needed to achieve the objective.

-----Sample Input-----
5 100 90 80
98
40
30
21
80

-----Sample Output-----
23

We are obtaining three bamboos of lengths 100, 90, 80 from five bamboos 98, 40, 30, 21, 80. We already have a bamboo of length 80, and we can obtain bamboos of lengths 100, 90 by using the magics as follows at the total cost of 23 MP, which is optimal.
 - Use Extension Magic twice on the bamboo of length 98 to obtain a bamboo of length 100. (MP consumed: 2)
 - Use Composition Magic on the bamboos of lengths 40, 30 to obtain a bamboo of length 70. (MP consumed: 10)
 - Use Shortening Magic once on the bamboo of length 21 to obtain a bamboo of length 20. (MP consumed: 1)
 - Use Composition Magic on the bamboo of length 70 obtained in step 2 and the bamboo of length 20 obtained in step 3 to obtain a bamboo of length 90. (MP consumed: 10)
"""

def minimum_mp_needed(N, A, B, C, lengths):
    from itertools import combinations

    def dfs(index, a, b, c):
        if index == N:
            if min(a, b, c) > 0:
                return abs(a - A) + abs(b - B) + abs(c - C) - 30
            else:
                return float('inf')
        
        # Do not use the current bamboo
        mp_not_used = dfs(index + 1, a, b, c)
        
        # Use the current bamboo for A
        mp_used_for_a = dfs(index + 1, a + lengths[index], b, c) + 10
        
        # Use the current bamboo for B
        mp_used_for_b = dfs(index + 1, a, b + lengths[index], c) + 10
        
        # Use the current bamboo for C
        mp_used_for_c = dfs(index + 1, a, b, c + lengths[index]) + 10
        
        return min(mp_not_used, mp_used_for_a, mp_used_for_b, mp_used_for_c)

    return dfs(0, 0, 0, 0)