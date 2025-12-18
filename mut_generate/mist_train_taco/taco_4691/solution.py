"""
QUESTION:
A big diamond is hidden in one of N identical bags. A balance scale is being used to determine which bag is the heaviest in order to locate the diamond. Find the minimum number of time you need to use the balance scale to find the bag containing the diamond.
Example 1:
Input:
N = 3
Output: 1
Explaination: 
The balance scale is needed only once. 
Take any two bags and put them on the 
scale. Either one of them will turn out 
to be heavier or they will be of equal 
weight and the left out third bag will 
contain the diamond.
Example 2:
Input:
N = 10
Output: 3
Explaination: 
The balance scale is needed 3 times. 
1st Put 5 bags on each side and determine 
which side is heavier. Take those 5 bags 
and put 2 on one side and 2 on the other 
leaving 1 out of the balance scale. If the 
scale is perfectly balanced, then the left 
out bag has teh diamond. Otherwise if one 
side is heavier, put those two in the balance. 
Your Task:
You do not need to read input or print anything. Your task is to complete the function minScale() which takes N as input parameter and returns the minimum number of times you need to use the balance scale to get the bag with diamond.
Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{6}
"""

def min_scale_uses(N: int) -> int:
    if N == 1:
        return 0
    if N == 2 or N == 3:
        return 1
    
    count = 0
    prod = 1
    
    while prod < N:
        count += 1
        prod *= 3
    
    return count