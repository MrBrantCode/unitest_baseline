"""
QUESTION:
Create a function named "sort_students" that takes a list of students with their full names as input and returns the sorted list. The sorting should be done based on the last name, and if two students have the same last name, they should be sorted by their first name. If the first names are also the same, they should be sorted by the length of their first name in ascending order. The function should implement a stable sorting algorithm with a time complexity of O(n log n) without using any built-in sorting functions or libraries.
"""

def sort_students(students):
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i].split()[-1] < right[j].split()[-1]:
                result.append(left[i])
                i += 1
            elif left[i].split()[-1] > right[j].split()[-1]:
                result.append(right[j])
                j += 1
            else:
                if left[i].split()[0] < right[j].split()[0]:
                    result.append(left[i])
                    i += 1
                elif left[i].split()[0] > right[j].split()[0]:
                    result.append(right[j])
                    j += 1
                else:
                    if len(left[i].split()[0]) < len(right[j].split()[0]):
                        result.append(left[i])
                        i += 1
                    else:
                        result.append(right[j])
                        j += 1
        
        while i < len(left):
            result.append(left[i])
            i += 1
        
        while j < len(right):
            result.append(right[j])
            j += 1
        
        return result
    
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        left = merge_sort(left)
        right = merge_sort(right)
        
        return merge(left, right)
    
    return merge_sort(students)