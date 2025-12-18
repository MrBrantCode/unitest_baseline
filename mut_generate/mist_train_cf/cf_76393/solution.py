"""
QUESTION:
Implement a function named `segregate_sort` that sorts a list containing a mix of integers and strings in ascending order, without using built-in sort functions. The function should be optimized for better time complexity than the regular bubble sort (O(n^2)) and treat all strings as lowercase. The function should return the sorted list with integers first, followed by the sorted strings.
"""

def segregate_sort(input_list):
    # Segregate numeric and alphanumeric elements
    num_list = [i for i in input_list if isinstance(i, int)]
    alpha_list = [i.lower() for i in input_list if isinstance(i, str)]

    # Optimized Bubble Sort for numeric elements
    for i in range(len(num_list)):
        swapped = False
        for j in range(len(num_list)-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                swapped = True
        if not swapped: break

    # Optimized Bubble Sort for alphanumeric elements
    for i in range(len(alpha_list)):
        swapped = False
        for j in range(len(alpha_list)-i-1):
            if alpha_list[j] > alpha_list[j+1]:
                alpha_list[j], alpha_list[j+1] = alpha_list[j+1], alpha_list[j]
                swapped = True
        if not swapped: break

    return num_list + alpha_list