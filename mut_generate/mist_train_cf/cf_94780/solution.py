"""
QUESTION:
Implement a function `sort_tuples` that sorts a list of tuples in a specific order. The tuples should be sorted based on the second element in descending order. If two tuples have the same second element, they should be sorted based on the third element in ascending order. If two tuples have the same second and third elements, they should be sorted based on the first element in descending order. You must implement this without using any built-in sorting functions or methods, and the solution should have a time complexity of O(n^2). Additionally, you are not allowed to use any additional data structures except for variables used for iteration and temporary storage.
"""

def sort_tuples(tuples_list):
    n = len(tuples_list)
    for i in range(n-1):
        for j in range(n-i-1):
            if tuples_list[j][1] < tuples_list[j+1][1]:
                tuples_list[j], tuples_list[j+1] = tuples_list[j+1], tuples_list[j]
            elif tuples_list[j][1] == tuples_list[j+1][1] and tuples_list[j][2] > tuples_list[j+1][2]:
                tuples_list[j], tuples_list[j+1] = tuples_list[j+1], tuples_list[j]
            elif tuples_list[j][1] == tuples_list[j+1][1] and tuples_list[j][2] == tuples_list[j+1][2] and tuples_list[j][0] < tuples_list[j+1][0]:
                tuples_list[j], tuples_list[j+1] = tuples_list[j+1], tuples_list[j]
    
    return tuples_list