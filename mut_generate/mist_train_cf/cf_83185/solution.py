"""
QUESTION:
Write a function named `advanced_sort` that takes a list of integers as input and returns a sorted list of integers. The function should attempt to sort the list by reversing any sublist or removing one or two elements from either end. If these attempts fail, the function should then try to sort the list by increasing or decreasing an element, and finally by swapping two elements. If all attempts fail, the function should return the original list.
"""

def advanced_sort(numbers):
    n = len(numbers)

    # If list is empty or already sorted, return it 
    if n == 0 or numbers == sorted(numbers):
        return numbers
    
    else:
        # Check every possible sublist from the original list, 
        # reverse the sublist and see if that makes the list sorted
        for i in range(n):
            for j in range(i+2, n+1):
                temp = numbers[i:j]
                temp.reverse()
                if numbers[0:i] + temp + numbers[j:] == sorted(numbers):
                    return sorted(numbers)

        # If we're here, it means attempting to sort by reversing sublists hasn't worked.
        # We will try removing elements.
        sorted_list = sorted(numbers)

        # Check after removing one or two elements 
        if sorted_list[1:] == sorted(sorted_list[1:]):
            return sorted_list[1:]
        elif sorted_list[:-1] == sorted(sorted_list[:-1]):
            return sorted_list[:-1]
        elif sorted_list[1:-1] == sorted(sorted_list[1:-1]):
            return sorted_list[1:-1]

        # If we're here, it means that even after removing elements, the list isn't sorted.
        # Then we try to by increasing/decreasing an element 
        # And we swap elements in order to rearrange the list in a sorted order 
        for i in range(1, n-1):
            if sorted_list[i-1] <= sorted_list[i] + 1 <= sorted_list[i+1]:
                sorted_list[i] = sorted_list[i] + 1
                if sorted_list == sorted(sorted_list):
                    return sorted_list
                
                # Revert the change just made
                sorted_list[i] = sorted_list[i] - 1
                
                if sorted_list[i-1] <= sorted_list[i] - 1 <= sorted_list[i+1]:
                    sorted_list[i] = sorted_list[i] - 1
                    if sorted_list == sorted(sorted_list):
                        return sorted_list
                    
                # Revert the change just made
                sorted_list[i] = sorted_list[i] + 1

                # Swap the two elements and check if the list is sorted
                sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]
                if sorted_list == sorted(sorted_list):
                    return sorted_list
                
                # If not sorted, revert the swap
                sorted_list[i], sorted_list[i+1] = sorted_list[i+1], sorted_list[i]

        return numbers  # If not possible, return the original list