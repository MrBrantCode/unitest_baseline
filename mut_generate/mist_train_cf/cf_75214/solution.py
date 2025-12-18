"""
QUESTION:
Create a function named `max_sum_list` that takes two lists of integers as input and returns the list with the maximum sum of elements. If both lists have the same sum, return a message indicating this. The function should handle exceptions where the inputs are not lists of integers.
"""

def max_sum_list(list1, list2):
    try:
        sum1 = sum(list1)
        sum2 = sum(list2)
        
        if sum1 > sum2:
            return list1
        elif sum2 > sum1:
            return list2
        else:
            return "Both lists have the same sum"
    
    except TypeError:
        return "Error: Both inputs should be lists of integers"

    except Exception as e:
        return f"An error occurred: {e}"