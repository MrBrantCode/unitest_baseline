"""
QUESTION:
Develop a program with a function named `arrayManipulation` that takes in three parameters: an array of integers, a list of operations, and a replace value 'x'. The function should first sort the array in ascending order without using any built-in sorting functions. Then, it should perform a list of operations on the sorted array. The operations can be 'Shift left', 'Sum and replace', or 'Reverse'. 'Shift left' moves each element to the left by one index and the first element moves to the end. 'Sum and replace' finds the sum of elements less than 'x' and replaces those elements with the sum. 'Reverse' reverses the array. The operations should be performed in the order they appear in the list. No built-in functions are allowed to perform these operations. The function should return the final array after all operations have been performed.
"""

def arrayManipulation(arr, operations, replace_x):
    # Bubble sort implementation to sort the array in ascending order
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    # Perform operations on the sorted array
    for operation in operations:
        if operation == 'Shift left':
            temp = arr[0]
            for i in range(len(arr)-1):
                arr[i] = arr[i + 1]
            arr[-1] = temp
        elif operation == 'Sum and replace':
            sum = 0
            for i in range(len(arr)):
                if arr[i] < replace_x:
                    sum += arr[i]
                    arr[i] = 0
            for i in range(len(arr)):
                if arr[i] == 0:
                    arr[i] = sum
        elif operation == 'Reverse':
            i = 0
            j = len(arr) - 1
            while(i < j):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
    return arr