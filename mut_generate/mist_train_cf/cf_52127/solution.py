"""
QUESTION:
Write a function `circularArrayLoop(nums)` that determines whether a cycle exists in the given circular array of non-zero integers `nums`. The function should return `True` if a cycle is found and `False` otherwise. The cycle must have a length greater than 1 and all elements in the cycle must have the same sign. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of `nums`. The length of `nums` is between 1 and 5000 (inclusive), and each element in `nums` is a non-zero integer between -1000 and 1000 (inclusive).
"""

def circularArrayLoop(nums):
    def getNext(cur):
        N = len(nums)
        next = (cur + nums[cur]) % N
        if next < 0:
            next += N
        if next == cur or nums[cur]*nums[next] < 0:
            return -1
        return next

    N = len(nums)
    for i, num in enumerate(nums):
        if num == 0:
            continue
            
        slow, fast = i, getNext(i)
        while slow != -1 and fast != -1 and slow != fast:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
      
        if slow != -1 and slow == fast:
            return True

    return False