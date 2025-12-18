"""
QUESTION:
Write a function named `find_kth_largest` that takes a list of numbers `mylist` and an integer `k` as parameters, and returns the Kth largest distinct value in the list without using any built-in sorting functions or methods. If `k` is larger than the length of the list or the number of distinct values, return `None`. The function should have a time complexity of O(N + KlogK), where N is the length of the list.
"""

def find_kth_largest(mylist, k):
    if k > len(mylist):
        return None
    
    distinct_values = set(mylist)
    sorted_values = []
    
    for num in distinct_values:
        for i in range(len(sorted_values)):
            if num > sorted_values[i]:
                sorted_values.insert(i, num)
                break
        else:
            sorted_values.append(num)
    
    if k > len(sorted_values):
        return None
    
    return sorted_values[k-1]