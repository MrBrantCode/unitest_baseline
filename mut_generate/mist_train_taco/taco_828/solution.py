"""
QUESTION:
Remember the story of Little Match Girl? By now, you know exactly what matchsticks the little match girl has, please find out a way you can make one square by using up all those matchsticks. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

 Your input will be several matchsticks the girl has, represented with their stick length. Your output will either be true or false, to represent whether you could make one square using all the matchsticks the little match girl has.

Example 1:

Input: [1,1,2,2,2]
Output: true

Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.



Example 2:

Input: [3,3,3,3,4]
Output: false

Explanation: You cannot find a way to form a square with all the matchsticks.



Note:

The length sum of the given matchsticks is in the range of 0 to 10^9.
The length of the given matchstick array will not exceed 15.
"""

def can_form_square(matchsticks):
    if len(matchsticks) < 4:
        return False
    total_length = sum(matchsticks)
    if total_length % 4 != 0:
        return False
    side_length = total_length // 4
    matchsticks.sort(reverse=True)
    if side_length < matchsticks[0]:
        return False
    
    def dfs(used, start_index, target, remain_rounds):
        if remain_rounds == 0:
            return True
        for i in range(start_index, len(matchsticks)):
            if i in used:
                continue
            num = matchsticks[i]
            if num > target:
                continue
            new_used = used | {i}
            if num == target:
                if dfs(new_used, 0, side_length, remain_rounds - 1):
                    return True
            else:
                if dfs(new_used, i + 1, target - num, remain_rounds):
                    return True
        return False
    
    return dfs(set(), 0, side_length, 4)