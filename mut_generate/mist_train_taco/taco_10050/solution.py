"""
QUESTION:
We are given non-negative integers nums[i] which are written on a chalkboard.  Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.  If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.  (Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)

Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.

Return True if and only if Alice wins the game, assuming both players play optimally.


Example:
Input: nums = [1, 1, 2]
Output: false
Explanation: 
Alice has two choices: erase 1 or erase 2. 
If she erases 1, the nums array becomes [1, 2]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.



Notes: 


       1 <= N <= 1000. 
       0 <= nums[i] <= 2^16.
"""

def alice_wins_game(nums):
    # Calculate the initial XOR of all elements in the list
    initial_xor = 0
    for num in nums:
        initial_xor ^= num
    
    # If the initial XOR is 0, Alice wins immediately
    if initial_xor == 0:
        return True
    
    # If the number of elements is odd, Alice will always lose
    # because she will be the one to erase the last element
    if len(nums) % 2 == 1:
        return False
    
    # If the number of elements is even, Alice can always force a win
    # by playing optimally
    return True