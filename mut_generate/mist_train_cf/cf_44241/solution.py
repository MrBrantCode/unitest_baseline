"""
QUESTION:
Design a function named `unique_3D_elements` that takes a three-dimensional array as input. The function should return a dictionary where the keys 'x', 'y', and 'z' represent the directions in the array, and the corresponding values are lists of elements that occur exactly once in their respective directions.
"""

def unique_3D_elements(array):
    result = {'x': [], 'y': [], 'z': []}
    for i in range(len(array)):
        x = set()
        y = set()
        z = set()
        for j in range(len(array[i])):
            for k in range(len(array[i][j])):
                if array[i][j][k] not in x:
                    x.add(array[i][j][k])
                if array[i][k][j] not in y:
                    y.add(array[i][k][j])
                if array[k][i][j] not in z:
                    z.add(array[k][i][j])
        result['x'].extend(list(x))
        result['y'].extend(list(y))
        result['z'].extend(list(z))
        
    # Remove duplicates from each direction
    result['x'] = list(set(result['x']))
    result['y'] = list(set(result['y']))
    result['z'] = list(set(result['z']))
    
    return result