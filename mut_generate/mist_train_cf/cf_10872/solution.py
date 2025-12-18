"""
QUESTION:
Write a function called `heap_sort` to sort an array of integers in ascending order using the heap sort technique. The time complexity should be less than O(n^2) and the space complexity should be less than O(n).
"""

def heap_sort(nums):
    """
    Sorts an array of integers in ascending order using the heap sort technique.

    Args:
    nums (list): A list of integers.

    Returns:
    list: The sorted list of integers.
    """

    def heapify(nums, n, i):
        """
        Performs the heapify operation on the binary heap.

        Args:
        nums (list): A list of integers.
        n (int): The size of the heap.
        i (int): The index of the current element.
        """
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if the left child exists and is greater than the current element
        if left < n and nums[left] > nums[largest]:
            largest = left

        # Check if the right child exists and is greater than the current element
        if right < n and nums[right] > nums[largest]:
            largest = right

        # If the largest element is not the current element, swap them
        if largest != i:
            nums[i], nums[largest] = nums[largest], nums[i]
            heapify(nums, n, largest)

    n = len(nums)

    # Build a binary heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)

    # Sort the binary heap
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heapify(nums, i, 0)

    return nums