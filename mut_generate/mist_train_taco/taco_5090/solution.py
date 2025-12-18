"""
QUESTION:
The king's birthday dinner was attended by $k$ guests. The dinner was quite a success: every person has eaten several dishes (though the number of dishes was the same for every person) and every dish was served alongside with a new set of kitchen utensils.

All types of utensils in the kingdom are numbered from $1$ to $100$. It is known that every set of utensils is the same and consist of different types of utensils, although every particular type may appear in the set at most once. For example, a valid set of utensils can be composed of one fork, one spoon and one knife.

After the dinner was over and the guests were dismissed, the king wondered what minimum possible number of utensils could be stolen. Unfortunately, the king has forgotten how many dishes have been served for every guest but he knows the list of all the utensils left after the dinner. Your task is to find the minimum possible number of stolen utensils.


-----Input-----

The first line contains two integer numbers $n$ and $k$ ($1 \le n \le 100, 1 \le k \le 100$)  — the number of kitchen utensils remaining after the dinner and the number of guests correspondingly.

The next line contains $n$ integers $a_1, a_2, \ldots, a_n$ ($1 \le a_i \le 100$)  — the types of the utensils remaining. Equal values stand for identical utensils while different values stand for different utensils.


-----Output-----

Output a single value — the minimum number of utensils that could be stolen by the guests.


-----Examples-----
Input
5 2
1 2 2 1 3

Output
1

Input
10 3
1 3 3 1 3 5 5 5 5 100

Output
14



-----Note-----

In the first example it is clear that at least one utensil of type $3$ has been stolen, since there are two guests and only one such utensil. But it is also possible that every person received only one dish and there were only six utensils in total, when every person got a set $(1, 2, 3)$ of utensils. Therefore, the answer is $1$.

One can show that in the second example at least $2$ dishes should have been served for every guest, so the number of utensils should be at least $24$: every set contains $4$ utensils and every one of the $3$ guests gets two such sets. Therefore, at least $14$ objects have been stolen. Please note that utensils of some types (for example, of types $2$ and $4$ in this example) may be not present in the set served for dishes.
"""

import math

def calculate_minimum_stolen_utensils(n, k, utensils):
    utensil_count = [0] * 100  # Initialize a list to count occurrences of each utensil type
    for utensil in utensils:
        utensil_count[utensil - 1] += 1
    
    max_utensil_per_guest = 0
    distinct_utensil_types = 0
    
    for count in utensil_count:
        if count > 0:
            distinct_utensil_types += 1
            max_utensil_per_guest = max(max_utensil_per_guest, math.ceil(count / k))
    
    total_utensils_needed = max_utensil_per_guest * distinct_utensil_types * k
    return total_utensils_needed - n