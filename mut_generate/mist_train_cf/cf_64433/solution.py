"""
QUESTION:
Design a function called `shell_sort` that takes a list of mixed data types (integers and strings) as input, sorts integers in ascending order and strings in dictionary order, and returns the sorted list. The function should maintain the original order in case of duplicates and treat integers and strings as different elements even if they have the same value. The input list can be empty or contain a single element.
"""

def shell_sort(raw_list):
    # separate numbers and strings
    num_list = [i for i in raw_list if isinstance(i, int)]
    str_list = [i for i in raw_list if isinstance(i, str)]
    lists = [num_list, str_list]

    for a_list in lists:
        n = len(a_list)
        gap = n//2

        # shell sort
        while gap > 0:
            for i in range(gap, n):
                temp = a_list[i]
                j = i
                while j >= gap and a_list[j-gap] > temp:
                    a_list[j] = a_list[j-gap]
                    j -= gap

                a_list[j] = temp
            gap //= 2

    return num_list + str_list