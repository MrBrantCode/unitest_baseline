"""
QUESTION:
Alice has a hand of cards, given as an array of integers.
Now she wants to rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.
Return true if and only if she can.
 


Example 1:
Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
Example 2:
Input: hand = [1,2,3,4,5], W = 4
Output: false
Explanation: Alice's hand can't be rearranged into groups of 4.

 
Constraints:

1 <= hand.length <= 10000
0 <= hand[i] <= 10^9
1 <= W <= hand.length

Note: This question is the same as 1296: https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
"""

from collections import Counter, deque
from typing import List

def can_form_consecutive_groups(hand: List[int], W: int) -> bool:
    if len(hand) % W != 0:
        return False
    
    q = deque()
    opened = 0
    last = 0
    counter = Counter(hand)
    
    for n in sorted(counter):
        count = counter[n]
        if n > last + 1 and opened > 0:
            return False
        if n == last + 1 and count < opened:
            return False
        q.append(count - opened)
        opened = count
        if len(q) == W:
            opened -= q.popleft()
        last = n
    
    return not opened