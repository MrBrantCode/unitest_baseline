"""
QUESTION:
To get money for a new aeonic blaster, ranger Qwerty decided to engage in trade for a while. He wants to buy some number of items (or probably not to buy anything at all) on one of the planets, and then sell the bought items on another planet. Note that this operation is not repeated, that is, the buying and the selling are made only once. To carry out his plan, Qwerty is going to take a bank loan that covers all expenses and to return the loaned money at the end of the operation (the money is returned without the interest). At the same time, Querty wants to get as much profit as possible.

The system has n planets in total. On each of them Qwerty can buy or sell items of m types (such as food, medicine, weapons, alcohol, and so on). For each planet i and each type of items j Qwerty knows the following:

  * aij — the cost of buying an item; 
  * bij — the cost of selling an item; 
  * cij — the number of remaining items.



It is not allowed to buy more than cij items of type j on planet i, but it is allowed to sell any number of items of any kind.

Knowing that the hold of Qwerty's ship has room for no more than k items, determine the maximum profit which Qwerty can get.

Input

The first line contains three space-separated integers n, m and k (2 ≤ n ≤ 10, 1 ≤ m, k ≤ 100) — the number of planets, the number of question types and the capacity of Qwerty's ship hold, correspondingly.

Then follow n blocks describing each planet.

The first line of the i-th block has the planet's name as a string with length from 1 to 10 Latin letters. The first letter of the name is uppercase, the rest are lowercase. Then in the i-th block follow m lines, the j-th of them contains three integers aij, bij and cij (1 ≤ bij < aij ≤ 1000, 0 ≤ cij ≤ 100) — the numbers that describe money operations with the j-th item on the i-th planet. The numbers in the lines are separated by spaces.

It is guaranteed that the names of all planets are different.

Output

Print a single number — the maximum profit Qwerty can get.

Examples

Input

3 3 10
Venus
6 5 3
7 6 5
8 6 10
Earth
10 9 0
8 6 4
10 9 3
Mars
4 3 0
8 4 12
7 2 5


Output

16

Note

In the first test case you should fly to planet Venus, take a loan on 74 units of money and buy three items of the first type and 7 items of the third type (3·6 + 7·8 = 74). Then the ranger should fly to planet Earth and sell there all the items he has bought. He gets 3·9 + 7·9 = 90 units of money for the items, he should give 74 of them for the loan. The resulting profit equals 16 units of money. We cannot get more profit in this case.
"""

def calculate_max_profit(n, m, k, buying_prices, selling_prices, item_counts):
    def get_profit(i, j):
        def take_first(z):
            return z[0]
        
        profits = []
        for w in range(m):
            profits.append((selling_prices[j][w] - buying_prices[i][w], item_counts[i][w]))
        
        profits.sort(key=take_first, reverse=True)
        
        count = 0
        profit = 0
        for w in profits:
            if count >= k:
                break
            profit += min(w[1], k - count) * max(w[0], 0)
            if w[0] > 0:
                count += min(w[1], k - count)
        
        return profit
    
    max_profit = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                max_profit = max(max_profit, get_profit(i, j))
    
    return max_profit