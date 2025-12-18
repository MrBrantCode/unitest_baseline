"""
QUESTION:
Create two separate functions, `bubble_sort` and `sort_string`, to sort two unordered lists in descending order. The first list contains integers and the second list contains strings. The `bubble_sort` function should implement an optimized bubble sort algorithm to sort the integer list, and the `sort_string` function should implement a sorting algorithm from scratch without using any Python built-in sort functionality to sort the string list alphabetically, considering case sensitivity. Finally, combine the two sorted lists into one list, with the sorted string list followed by the sorted integer list. The function should handle lists of varying lengths and elements.
"""

def entrance(nums, st):
    # bubble sort function to sort integer list
    def bubble_sort(nums):
        swap_happened = True
        while swap_happened:
            swap_happened = False
            for i in range(len(nums) - 1):
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swap_happened = True
        return nums

    # implement sorting algorithm from scratch to sort the string list
    def sort_string(st):
        for i in range(len(st)):
            for j in range(i+1, len(st)):
                if st[i].lower() > st[j].lower():
                    st[i], st[j] = st[j], st[i]
                elif st[i].lower() == st[j].lower() and st[i] > st[j]:  
                    st[i], st[j] = st[j], st[i]
        return st[::-1]  

    nums = bubble_sort(nums)
    st = sort_string(st)
    return st + nums