"""
QUESTION:
Write a function `merge_sorted_lists` that merges two sorted lists of distinct integers into a single sorted list. The function should not use any built-in sorting or merging functions. The output should also remove any repeated horizontal sequences. The function should take two lists of integers as input and return a single list of integers. Assume that the input lists are sorted in ascending order and contain only distinct integers.
"""

def merge_sorted_lists(list1, list2):
    # Initialize an empty list to store the merged list
    merged_list = []
    i = 0
    j = 0
    
    # Loop until all items are processed from both lists
    while i < len(list1) and j < len(list2):
        # If item in list1 is lesser, append it to the merged list and move pointer in list1
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        # If item in list2 is lesser, append it to the merged list and move pointer in list2    
        elif list1[i] > list2[j]:
            merged_list.append(list2[j])
            j += 1
        # If both items are same, append only once and move both pointers
        else:
            merged_list.append(list1[i])
            i += 1
            j += 1

    # If there are remaining items in list1, append them to the merged list
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # If there are remaining items in list2, append them to the merged list
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    # Ensure to remove repeated horizontal sequences (if any)
    final_list = [merged_list[0]]
    for k in range(1, len(merged_list)):
        if merged_list[k] != merged_list[k-1]:
            final_list.append(merged_list[k])

    return final_list