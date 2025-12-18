"""
QUESTION:
You are given 'k' eggs and a 'n' storey building. The eggs MIGHT break if thrown down from a specific height (Note: It is NOT necessary that the eggs have to break; they might not even break from the topmost floor). What is the minimum number of steps in which you can find (using 'k' eggs) the minimum height of the floor in the building from which the eggs will start breaking ? 

Note: 

You have to output the minimum number of steps required; NOT the floor of the building from which eggs will break;

Input Format: 

First line of the input is an integer 'q':
1 ≤ q ≤ 1,000, which is the number of queries. 

Second line of the input has two space separated integers: the height of the building 'n' and the number of eggs which you can use 'k':
1 ≤ n ≤ 1,000
1 ≤ k ≤ 10

Output Format:

For each q output a single line denoting the minimum number of trials required to find the height from which the eggs will start breaking. 

Example:

For n = 151 and k = 1 the minimum number of steps in which we can find the height from which eggs can break(considering the worst case) is 151. This is because since we have only 1 egg we have no choice but to start from the first floor and throw the egg from each floor and check whether it breaks or not. In worst case this might require 151 steps. 

For n = 100 and k = 2 the minimum number of steps in which we can find the height from which eggs can break(considering again the worst case) is 14. This is because suppose we throw the FIRST egg from 14th floor and it breaks then we will have to try each of the remaining 13 floors using the remaining egg. So in this case number of trials required is 14. Suppose the first egg doesn't break then we can drop it from 27th floor (13 + 14). We have chosen 27th floor because suppose if the first egg breaks from 27th floor then we will have to test floors from 15-26 (=12). So, the total number of trials required in this case is: 12 + 1(from 14th floor) + 1(from 27th floor) = 14 trials. Suppose the first egg doesn't break even now, drop it from 39(12 + 13 + 14) floor for same reason. 

SAMPLE INPUT
4
10 1
10 2
100 2
104 3

SAMPLE OUTPUT
10
4
14
9
"""

def min_steps_to_find_critical_floor(k: int, n: int) -> int:
    """
    Calculate the minimum number of steps required to find the critical floor in a building
    using 'k' eggs and a building of height 'n'.

    Parameters:
    k (int): The number of eggs available.
    n (int): The height of the building.

    Returns:
    int: The minimum number of steps required to find the critical floor.
    """
    ht = {}
    
    def floors(e, s):
        if e == 0 or s == 0:
            return 0
        elif e == 1:
            return s
        elif s == 1:
            return 1
        elif e > s:
            return floors(s, s)
        if (e, s) not in ht:
            ht[(e, s)] = floors(e-1, s-1) + floors(e, s-1) + 1
        return ht[(e, s)]
    
    s = 0
    while floors(k, s) < n:
        s += 1
    return s