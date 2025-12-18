"""
QUESTION:
Consider the following game. There are k pairs of n cards with numbers from 1 to n written one by one. Shuffle these kn cards well to make piles of k cards and arrange them in a horizontal row. The i-th (k-card) pile from the left of the n piles created in this way is called "mountain i".

<image>


The game starts at mountain 1. Draw the top card of the pile (the drawn card is not returned to the original pile), and if the number written on that card is i, draw the top card of the pile i Pull. In this way, draw the top card of the pile numbered by the number written on the drawn card repeatedly, and if all the piles have no cards, it is successful. If there are still piles of cards left, but there are no more piles to draw next, it is a failure.

If it fails in the middle, it ends with a failure, or the remaining card pile is left as it is (the pile number is also kept as it is) and the game is restarted. When restarting the game, the first card to draw is from the leftmost pile of the remaining piles (the top card of that pile is the first card to be drawn). After resuming, proceed with the game in the same way as before resuming, and if there are no cards in all the piles, it is a success. It is a failure.

<image>


Such a game shall be restarted up to m times. However, m is 0 or 1. In other words, it either does not restart once or restarts only once. The initial placement of cards differs depending on how you shuffle before the game starts. Of course, depending on the initial placement of the card, it may succeed without resuming, it may resume and succeed, or it may resume and fail. Since it is shuffled enough, we assume that all initial arrangements appear with the same probability, and we want to find the probability p that the restart will succeed within m times. Express this probability p as a decimal number, and create a program that finds and outputs to the decimal place r. However, output so that the following conditions are met.

* If p × 10K becomes an integer when a sufficiently large positive integer K is taken, 0 continues from the middle of the decimal part, but that 0 should also be output. For example, if p = 3/8 = 0.375, then 0.37500 is output if r = 5, and 0.37 is output if r = 2. Similarly, when p = 1.0, for example, if r = 3, output 1.000.
* For example, 0.150000 ... can be expressed as a recurring decimal 0.1499999 ..., but in such a case, the former expression is used.



On the first line of the input file, the integers n, k, m, and r are written in this order with a blank as the delimiter. 1 ≤ n ≤ 10000, 1 ≤ k ≤ 100, m = 0 or m = 1, 1 ≤ r ≤ 10000.

Input example 1 | Input example 2 | Input example 3
--- | --- | ---
|
2 1 0 5 | 3 1 1 3 | 2 2 1 3 |
Output example 1 | Output example 2 | Output example 3
0.50000 | 0.833 | 1.000 |

input

The input consists of multiple datasets. Input ends when n, k, m, and r are all 0. The number of datasets does not exceed 5.

output

For each dataset, p is output on one line as specified.





Example

Input

2 1 0 5
3 1 1 3
2 2 1 3
0 0 0 0


Output

0.50000
0.833
1.000
"""

from decimal import Decimal, Context, ROUND_HALF_UP, setcontext

def calculate_success_probability(n, k, m, r):
    if n == 0:
        return ""
    
    setcontext(Context(prec=r, rounding=ROUND_HALF_UP))
    one = Decimal(1)
    ans = one / Decimal(n)
    
    if m == 1:
        s = 0
        for i in range(1, n):
            s += one / Decimal(i)
        ans *= 1 + s
    
    ans = str(ans)[:r + 2]
    if len(ans) < r + 2:
        ans += '0' * (r + 2 - len(ans))
    
    return ans