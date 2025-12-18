"""
QUESTION:
Write a function `control_print` that takes two 2D arrays of integers, `main_array` and `control_array`, as input and prints the elements of `main_array` according to the directions specified in `control_array`. If the corresponding value in `control_array` is 1, print the corresponding row in `main_array` in reverse order. If it's 0, print the row in the default order. If the sum of elements in a row in `control_array` is greater than 2, do not print that row from `main_array`. The function should check if `main_array` and `control_array` have the same dimensions, and if not, print an error message and return.
"""

def control_print(main_array, control_array):
    # check if the lengths of main_array and control_array are equal
    if len(main_array) != len(control_array):
        print("Error: The main array and control array do not have the same dimensions.")
        return

    # check if each row of main_array and control_array are of equal length
    for i in range(len(main_array)):
        if len(main_array[i]) != len(control_array[i]):
            print("Error: The main array and control array do not have the same dimensions.")
            return

    # scan through each row
    for i in range(len(main_array)):
        # calculate sum of elements in control_array's row
        row_sum = sum(control_array[i])

        # if row_sum > 2, do not print the corresponding row from main_array
        if row_sum > 2:
            continue

        # print elements of the row of the main array
        for j in range(len(main_array[i])):
            # if corresponding value in control_array is 1, print elements in reverse order
            if control_array[i][j] == 1:
                print(main_array[i][::-1][j], end=' ')
            # if corresponding value in control_array is 0, print elements in default order
            elif control_array[i][j] == 0:
                print(main_array[i][j], end=' ')
        # print newline for next row
        print()