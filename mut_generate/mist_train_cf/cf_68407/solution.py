"""
QUESTION:
Implement a class `ComputedArray` with the following methods:

- `__init__(self, nums)`: Initializes the data structure using the given integer array `nums`.
- `update(self, i, val)`: Updates the integer at position `i` in the original array to `val` and revises the computed array.
- `getResult(self)`: Returns the current computed array.

Constraints:

- The initial integer array will not contain zero.
- The solution must have a time complexity better than O(n²) for the update operation.
- Division operation is not allowed.
"""

def ComputedArray(nums):
    class ComputedArray:
        def __init__(self):
            self.nums = nums
            self.computed = [0 for _ in nums]
            self.prefix = [1 for _ in nums]
            self.postfix = [1 for _ in nums]
            self.build()

        def build(self):
            n = len(self.nums)
            for i in range(1,n):
                self.prefix[i] = self.prefix[i-1]*self.nums[i-1]
            for i in range(n-2,-1,-1):
                self.postfix[i] = self.postfix[i+1]*self.nums[i+1]
            for i in range(n):
                self.computed[i] = self.prefix[i]*self.postfix[i]

        def update(self, idx, val):
            old_val = self.nums[idx]
            self.nums[idx] = val
            for i in range(idx, len(self.nums)):
                self.prefix[i] = self.prefix[i] // old_val * val
            for i in range(idx, -1, -1):
                self.postfix[i] = self.postfix[i] // old_val * val
            for i in range(len(self.nums)):
                self.computed[i] = self.prefix[i]*self.postfix[i]

        def getResult(self):
            return self.computed
    return ComputedArray()