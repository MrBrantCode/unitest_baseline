"""
QUESTION:
Create a function `build_min_heap` that takes an array of integers as input and returns the array converted into a min-heap. The function should have a time complexity of O(N) and a space complexity of O(log N). If the input array contains duplicate elements, the function should maintain their original order within the min-heap.
"""

def build_min_heap(nums):
    """
    Convert an array of integers into a min-heap.

    Args:
        nums (list): The input array of integers.

    Returns:
        list: The input array converted into a min-heap.

    Time complexity: O(N)
    Space complexity: O(log N)
    """
    def heapify(i):
        # Find the left and right child indices
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        # Initialize the smallest element index as the current index
        smallest = i

        # Check if the left child is smaller than the current element
        if left_child < len(nums) and nums[left_child] < nums[smallest]:
            smallest = left_child

        # Check if the right child is smaller than the current element
        if right_child < len(nums) and nums[right_child] < nums[smallest]:
            smallest = right_child

        # If the smallest element index is different from the current index, swap the elements
        if smallest != i:
            nums[i], nums[smallest] = nums[smallest], nums[i]
            heapify(smallest)

    # Start from the last non-leaf node and perform heapify
    for i in range(len(nums) // 2 - 1, -1, -1):
        heapify(i)

    return nums