"""
QUESTION:
Ryouko is an extremely forgetful girl, she could even forget something that has just happened. So in order to remember, she takes a notebook with her, called Ryouko's Memory Note. She writes what she sees and what she hears on the notebook, and the notebook became her memory.

Though Ryouko is forgetful, she is also born with superb analyzing abilities. However, analyzing depends greatly on gathered information, in other words, memory. So she has to shuffle through her notebook whenever she needs to analyze, which is tough work.

Ryouko's notebook consists of n pages, numbered from 1 to n. To make life (and this problem) easier, we consider that to turn from page x to page y, |x - y| pages should be turned. During analyzing, Ryouko needs m pieces of information, the i-th piece of information is on page ai. Information must be read from the notebook in order, so the total number of pages that Ryouko needs to turn is <image>.

Ryouko wants to decrease the number of pages that need to be turned. In order to achieve this, she can merge two pages of her notebook. If Ryouko merges page x to page y, she would copy all the information on page x to y (1 ≤ x, y ≤ n), and consequently, all elements in sequence a that was x would become y. Note that x can be equal to y, in which case no changes take place.

Please tell Ryouko the minimum number of pages that she needs to turn. Note she can apply the described operation at most once before the reading. Note that the answer can exceed 32-bit integers.

Input

The first line of input contains two integers n and m (1 ≤ n, m ≤ 105).

The next line contains m integers separated by spaces: a1, a2, ..., am (1 ≤ ai ≤ n).

Output

Print a single integer — the minimum number of pages Ryouko needs to turn.

Examples

Input

4 6
1 2 3 4 3 2


Output

3


Input

10 5
9 4 3 8 8


Output

6

Note

In the first sample, the optimal solution is to merge page 4 to 3, after merging sequence a becomes {1, 2, 3, 3, 3, 2}, so the number of pages Ryouko needs to turn is |1 - 2| + |2 - 3| + |3 - 3| + |3 - 3| + |3 - 2| = 3.

In the second sample, optimal solution is achieved by merging page 9 to 4.
"""

def calculate_minimum_page_turns(n, m, pages):
    def median(a):
        if len(a) == 0:
            return 0
        if len(a) % 2 == 1:
            return a[len(a) // 2]
        else:
            return (a[len(a) // 2] + a[len(a) // 2 - 1]) // 2

    def profit(a, old_val):
        a.sort()
        med = median(a)
        sum_old = 0
        sum_new = 0
        for i in a:
            sum_old += abs(i - old_val)
            sum_new += abs(i - med)
        return sum_old - sum_new

    count = {pages[0]: []}
    current_page_switches = 0

    for i in range(1, len(pages)):
        cur_i = pages[i]
        prev_i = pages[i - 1]
        if not cur_i in count:
            count[cur_i] = []
        if cur_i != prev_i:
            count[cur_i].append(prev_i)
            count[prev_i].append(cur_i)
            current_page_switches += abs(cur_i - prev_i)

    max_profit = 0
    for i in count:
        if len(count[i]) > 0:
            tmp = profit(count[i], i)
            if tmp > max_profit:
                max_profit = tmp

    min_page_turns = current_page_switches - max_profit
    return min_page_turns