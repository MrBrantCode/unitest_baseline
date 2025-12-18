"""
QUESTION:
Design a function named `counting_sort` that sorts an array of integers in ascending order. The function should take two parameters: `array1` (the array to be sorted) and `max_val` (the maximum possible value in the array). The function should be efficient for large arrays with a significant number of duplicate elements.
"""

def counting_sort(array1, max_val):
    m = max_val + 1
    count = [0] * m                

    for a in array1:
        # count occurences 
        count[a] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    return array1