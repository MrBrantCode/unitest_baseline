"""
QUESTION:
Implement a function `counting_sort` that sorts a list of integers in ascending order using the counting sort algorithm. The function should take two parameters: `array1` (a list of integers) and `max_val` (the maximum value in the list). The function should return the sorted list. Additionally, implement a function `print_repeat_count` that takes a sorted list of integers as input and prints each repeating number in the list along with its occurrence count.
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

def print_repeat_count(array):
    count_dict = {}
    for i in array:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    
    for k, v in count_dict.items():
        if v > 1:
            print("Number: {} , Occurrence: {}".format(k, v))