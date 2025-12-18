"""
QUESTION:
Create a class called `MyArray` that takes an array of elements as input. The class should be able to sort valid integers in the array in both ascending and descending order while excluding non-integer entries. The class should have the following methods: `sort_nums_ascending()`, `sort_nums_descending()`, `median()`, and `sum_nums()`. The `median()` method should calculate the median of the sorted integers, and the `sum_nums()` method should calculate the sum of all valid integers in the array. The class should handle exceptions by excluding non-numeric or non-integer inputs.
"""

def sort_and_calculate(nums):
    nums = [num for num in nums if isinstance(num, int)]
    nums.sort()
    
    def sort_nums_ascending():
        return nums
    
    def sort_nums_descending():
        return nums[::-1]
    
    def median():
        n = len(nums)
        middle = n // 2
        if n % 2 == 0:
            return (nums[middle - 1] + nums[middle]) / 2
        else:
            return nums[middle]
    
    def sum_nums():
        return sum(nums)
    
    return {
        "sort_nums_ascending": sort_nums_ascending(),
        "sort_nums_descending": sort_nums_descending(),
        "median": median(),
        "sum_nums": sum_nums()
    }