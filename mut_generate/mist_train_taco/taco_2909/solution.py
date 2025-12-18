"""
QUESTION:
There are several cards arranged in a row, and each has an associated number of points. The points are given in the integer array cardPoints of size N.
In one step, you can take one card from beginning or from the end of the row. You have to take exactly k cards.
Your score is the sum of the points of the cards you have taken.
Given the integer array cardPoints, and its size N and the integer k, return the maximum score you can obtain.
Example 1:
Input:
N = 7
k = 3
cardPoints[ ] = {1, 2, 3, 4, 5, 6, 1}
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the cards on the right, giving a final score of 1 + 6 + 5 = 12.
 
Example 2:
Input:
N = 5
k = 5
arr[ ] = {8, 6, 2, 4, 5}
Output: 25
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maxScore() which takes the array of integers cardPoints , an integer N and k as parameters and returns a maximum score.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ k ≤ N
^{1 }≤ cardPoints_{i  }≤ 10^{5}
"""

def max_score(cardPoints, k):
    N = len(cardPoints)
    startpoint = N - 1
    endpoint = k - 1
    rollingsum = sum(cardPoints[0:endpoint + 1])
    maxsum = rollingsum
    
    for i in range(k):
        rollingsum = rollingsum - cardPoints[endpoint] + cardPoints[startpoint]
        startpoint -= 1
        endpoint -= 1
        maxsum = max(maxsum, rollingsum)
    
    return maxsum