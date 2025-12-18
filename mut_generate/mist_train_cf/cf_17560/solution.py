"""
QUESTION:
Write a function named `sort_tuples` that sorts a list of tuples in-place. The list of tuples should be sorted based on the following conditions: 
- The second element of each tuple in descending order.
- If two tuples have the same second element, they should be sorted based on the third element in ascending order.
- If two tuples have the same second and third elements, they should be sorted based on the first element in descending order.

Restrictions: 
- Do not use any built-in sorting functions or methods.
- The implementation should have a time complexity of O(n^2).
- Do not use any additional data structures except for variables used for iteration and temporary storage.
"""

def sort_tuples(tuples_list):
    n = len(tuples_list)
    for i in range(n-1):
        for j in range(n-i-1):
            # Compare the second element of each tuple
            if tuples_list[j][1] < tuples_list[j+1][1]:
                tuples_list[j], tuples_list[j+1] = tuples_list[j+1], tuples_list[j]
            # If second elements are equal, compare the third element
            elif tuples_list[j][1] == tuples_list[j+1][1] and tuples_list[j][2] > tuples_list[j+1][2]:
                tuples_list[j], tuples_list[j+1] = tuples_list[j+1], tuples_list[j]
            # If second and third elements are equal, compare the first element
            elif tuples_list[j][1] == tuples_list[j+1][1] and tuples_list[j][2] == tuples_list[j+1][2] and tuples_list[j][0] < tuples_list[j+1][0]:
                tuples_list[j], tuples_list[j+1] = tuples_list[j+1], tuples_list[j]
    
    return tuples_list