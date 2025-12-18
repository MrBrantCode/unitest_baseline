"""
QUESTION:
Construct a function named `bubble_sort_mixed` that sorts a mixed list of integers and strings into two separate sorted lists: one for integers in ascending order and one for strings in ascending order with case-insensitivity. The function should return a combined list of the two sorted lists, with the integers first.
"""

def bubble_sort_mixed(arr):
    def bubble_sort(arr, op):
        n = len(arr)

        for i in range(n):
            switched = False
            for j in range(n - i - 1):

                if type(arr[j]) == str:
                    arr[j] = arr[j].lower()
                    arr[j + 1] = arr[j + 1].lower()

                if op == '<':
                    if arr[j] > arr[j + 1] :
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        switched = True
                else:
                    if arr[j] < arr[j + 1] :
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                        switched = True

            if switched == False:
                break

        return arr

    arr_numerics = [i for i in arr if type(i)!=str]
    arr_strings = [j for j in arr if type(j)==str]

    arr_numerics = bubble_sort(arr_numerics, '<')
    arr_strings = bubble_sort(arr_strings, '<')

    return arr_numerics + arr_strings