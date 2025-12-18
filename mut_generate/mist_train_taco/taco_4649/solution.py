"""
QUESTION:
Akash is good at mathematics and games. He also has a nature of boasting about it. He invites his best friend to dinner and ask him to play his newly invented game.
He presents N numbers and an integer K. The game goes like this:
Each player will be given turn one by one. In each of their turn they can choose any number (non-zero) from the given array and divide (Integer division) it with K. The player who is unable to complete his move looses. Akash is very confident about his skills and knowledge about the game so he gives the first chance to his friends.
 
Example 1:
Input: nums = [1, 2, 3], k = 2
Output: Akash
Explanation: Friend will choose 2, then numbers
will become [1, 1, 3]. Akash will choose 3, 
then numbers will become [1, 1, 1].Friend will 
choose 1 then numbers become [0, 1, 1]. Akash 
will choose 1 then numbers will become 
[0, 0, 1]. Friend will choose 1 then numbers 
will become [0, 0, 0]. Now akash can't make 
a move.
Example 2:
Input: nums = [2, 4, 6], k = 2
Output: Friend
Explanation: Akash will win the game.
 
Your Task:
You don't have to read or print anything. Your task is to complete the function Play() which takes the list of numbers as input parameter and returns "Akash" if his friend wins otherwise returns "Friend" (Without quotes).
 
Expected Time Complexity: O(n * c) where c is constant.
Expected Space Complexity: O(1)
 
Constraints:
1 <= n <= 100000
2 <= k <= 1000000
1 <= numbers <= 1000000
"""

def determine_winner(nums, k):
    x = 0
    for num in nums:
        g = num
        while g > 0:
            x += 1
            g = g // k
    if x % 2 == 1:
        return 'Akash'
    return 'Friend'