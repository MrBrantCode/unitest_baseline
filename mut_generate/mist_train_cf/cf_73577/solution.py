"""
QUESTION:
Write a function named `delete_index_3d` that takes a 3D array and an index as input, and returns the 3D array with the element at the specified index deleted. The index should be a list of three integers representing the indices at each level of the multidimensional array.
"""

def delete_index_3d(array, index):
    newArr = []
    for i in range(len(array)):
        if i == index[0]:
            newSubArr = []
            for j in range(len(array[i])):
                if j == index[1]:
                    newSubSubArr = []
                    for k in range(len(array[i][j])):
                        if k != index[2]:
                            newSubSubArr.append(array[i][j][k])
                    newSubArr.append(newSubSubArr)
                else:
                    newSubArr.append(array[i][j])
            newArr.append(newSubArr)
        else:
            newArr.append(array[i])
    return newArr