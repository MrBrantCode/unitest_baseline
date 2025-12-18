"""
QUESTION:
You are visiting a farm that has a single row of fruit trees arranged from left to right.The trees are represented by an integer array fruits of size N, where fruits[i]  is the type of fruit the ith tree produces.
You want to collect as much fruit as possible.However,the owner has some strict rules that you must follow :
	You only have two baskets , and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
	Starting from any tree of your choice,you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of the baskets.
	Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits , return the maximum number of fruits you can pick.
Example 1:
Input:
N = 3
fruits [ ] = { 2, 1, 2 }
Output: 3
Explanation: We can pick from all three trees. 
 
Example 2:
Input:
N = 6
fruits [ ] = { 0, 1, 2, 2, 2, 2 }
Output: 5
Explanation: It's optimal to pick from trees(0-indexed) [1,2,3,4,5].
Your Task:
You don't need to read input or print anything. Your task is to complete function totalFruits() which takes the integer array fruits and it's size N as input parameters and returns the maximum number of fruits the you can pick.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ fruits_{i} < N
"""

def totalFruits(fruits, N):
    if N == 0:
        return 0
    
    first = fruits[0]
    second = -1
    i = 0
    j = 1
    ans = 1
    
    while j < N:
        if fruits[j] != first and fruits[j] != second:
            if second == -1:
                second = fruits[j]
            else:
                i = j
                while fruits[i - 1] == fruits[j - 1]:
                    i -= 1
                if first != fruits[i]:
                    first = fruits[j]
                else:
                    second = fruits[j]
        ans = max(ans, j - i + 1)
        j += 1
    
    return ans