"""
QUESTION:
Implement a function `quick_sort` that sorts a list of alphanumeric data in lexicographic order. The function should take a list and its low and high indices as input. The list can contain both lowercase and uppercase letters, as well as numbers. The function should be able to handle any combination of these characters and sort them according to their ASCII values, with numbers coming before letters.
"""

# The main function that implements quickSort
def quick_sort(sort_list, low, high):
    # An important part of Quick Sort is the partition function
    # In the context of quicksort, "partitioning" works by selecting a pivot point in the array 
    # and moving every alphanumeric less than the pivot before it, and the ones greater after it.

    def partition(sort_list, low, high):
        i = (low -1)
        pivot = sort_list[high]
        for j in range(low, high):
            if sort_list[j] <= pivot:
                i += 1
                sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
        sort_list[i+1], sort_list[high] = sort_list[high], sort_list[i+1]
        return (i + 1)

    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi - 1)
        quick_sort(sort_list, pi + 1, high)