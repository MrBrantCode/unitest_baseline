"""
QUESTION:
Implement a function named `binary_indexed_tree` that represents a data structure which can be used to efficiently compute the sum of a given range of elements in an array. The time complexity of operations in this data structure should be O(logN), where N is the size of the array.
"""

class BinaryIndexedTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def get_sum(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def range_sum(self, start, end):
        return self.get_sum(end) - self.get_sum(start - 1)


def binary_indexed_tree(nums):
    bit = BinaryIndexedTree(len(nums))
    for i in range(len(nums)):
        bit.update(i + 1, nums[i])
    return bit