"""
QUESTION:
Construct a dice from a given sequence of integers in the same way as Dice I.

You are given integers on the top face and the front face after the dice was rolled in the same way as Dice I. Write a program to print an integer on the right side face.


<image>


Constraints

* $0 \leq $ the integer assigned to a face $ \leq 100$
* The integers are all different
* $1 \leq q \leq 24$

Input

In the first line, six integers assigned to faces are given in ascending order of their corresponding labels. In the second line, the number of questions $q$ is given.

In the following $q$ lines, $q$ questions are given. Each question consists of two integers on the top face and the front face respectively.

Output

For each question, print the integer on the right side face.

Example

Input

1 2 3 4 5 6
3
6 5
1 3
3 2


Output

3
5
6
"""

def find_right_side_faces(dice_faces, queries):
    """
    Given a dice configuration and a list of queries, returns the integer on the right side face for each query.

    Parameters:
    dice_faces (list of int): A list of six integers representing the dice faces in ascending order.
    queries (list of tuple): A list of tuples, each containing two integers representing the top and front faces for each query.

    Returns:
    list of int: A list of integers representing the right side face for each query.
    """
    
    def lotate(dic, dire):
        if dire == 'N':
            (x, y, z, w) = (dic['up'], dic['back'], dic['bottom'], dic['front'])
            (dic['back'], dic['bottom'], dic['front'], dic['up']) = (x, y, z, w)
        elif dire == 'S':
            (x, y, z, w) = (dic['up'], dic['back'], dic['bottom'], dic['front'])
            (dic['front'], dic['up'], dic['back'], dic['bottom']) = (x, y, z, w)
        elif dire == 'W':
            (x, y, z, w) = (dic['up'], dic['left'], dic['bottom'], dic['right'])
            (dic['left'], dic['bottom'], dic['right'], dic['up']) = (x, y, z, w)
        elif dire == 'E':
            (x, y, z, w) = (dic['up'], dic['left'], dic['bottom'], dic['right'])
            (dic['right'], dic['up'], dic['left'], dic['bottom']) = (x, y, z, w)
        return dic
    
    results = []
    for x, y in queries:
        dic = {'up': dice_faces[0], 'front': dice_faces[1], 'right': dice_faces[2], 
               'left': dice_faces[3], 'back': dice_faces[4], 'bottom': dice_faces[5]}
        s = 'EEENEEENEEESEEESEEENEEEN'
        for i in s:
            if dic['up'] == x and dic['front'] == y:
                results.append(dic['right'])
                break
            dic = lotate(dic, i)
    
    return results