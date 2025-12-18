"""
QUESTION:
Write a function called `sort_array` that sorts an array of arrays in descending order. Each inner array contains a mix of strings and integers, but only the strings should be used for sorting purposes. The sorting should be done in descending alphabetical order of the strings. If two inner arrays have the same string elements, they should be sorted based on the sum of their integer elements.
"""

def sort_array(arr):
    n = len(arr)

    # Two separate loops are being used to loop over the array
    for i in range(n):
        for j in range(0, n-i-1):

            # Separate lists for storing strings and integers
            str_list1 = sorted([str(i) for i in arr[j] if isinstance(i, str)], reverse=True)
            int_list1 = sum([i for i in arr[j] if isinstance(i, int)])
            str_list2 = sorted([str(i) for i in arr[j+1] if isinstance(i, str)], reverse=True)
            int_list2 = sum([i for i in arr[j+1] if isinstance(i, int)])

            # Comparing strings
            if str_list1 < str_list2:
              arr[j], arr[j+1] = arr[j+1], arr[j]
            # If strings are equal, comparing sum of integers
            elif str_list1 == str_list2:
              if int_list1 < int_list2:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr