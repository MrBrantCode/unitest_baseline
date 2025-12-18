"""
QUESTION:
Implement a function called `sortEvenNumbers` that takes a list of integers as input and sorts only the even numbers in ascending order. The function should maintain the original position of the odd numbers. The function should also handle potential errors and print meaningful error messages. The input list can contain both positive and negative numbers.
"""

def sortEvenNumbers(array):
    try:
        indexes = [i for i, num in enumerate(array) if num % 2 == 0]
        def partition(array, low, high, indexes):
            i = low - 1
            pivot = array[indexes[high]]

            for j in range(low, high):
                if array[indexes[j]] <= pivot:
                    i += 1
                    indexes[i], indexes[j] = indexes[j], indexes[i]

            indexes[i+1], indexes[high] = indexes[high], indexes[i+1]
            return (i+1)

        def quickSort(array, low, high, indexes):
            if low < high:
                pi = partition(array, low, high, indexes)
                quickSort(array, low, pi-1, indexes)
                quickSort(array, pi+1, high, indexes)

        quickSort(array, 0, len(indexes)-1, indexes)

        output = array.copy()
        for i, index in enumerate(indexes):
            output[index] = array[indexes[i]]

        return output
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")