"""
QUESTION:
You are given a set of points on a straight line. Each point has a color assigned to it. For point a, its neighbors are the points which don't have any other points between them and a. Each point has at most two neighbors - one from the left and one from the right.

You perform a sequence of operations on this set of points. In one operation, you delete all points which have a neighbor point of a different color than the point itself. Points are deleted simultaneously, i.e. first you decide which points have to be deleted and then delete them. After that you can perform the next operation etc. If an operation would not delete any points, you can't perform it.

How many operations will you need to perform until the next operation does not have any points to delete?


-----Input-----

Input contains a single string of lowercase English letters 'a'-'z'. The letters give the points' colors in the order in which they are arranged on the line: the first letter gives the color of the leftmost point, the second gives the color of the second point from the left etc.

The number of the points is between 1 and 10^6.


-----Output-----

Output one line containing an integer - the number of operations which can be performed on the given set of points until there are no more points to delete.


-----Examples-----
Input
aabb

Output
2

Input
aabcaa

Output
1



-----Note-----

In the first test case, the first operation will delete two middle points and leave points "ab", which will be deleted with the second operation. There will be no points left to apply the third operation to.

In the second test case, the first operation will delete the four points in the middle, leaving points "aa". None of them have neighbors of other colors, so the second operation can't be applied.
"""

def count_operations_until_stable(points: str) -> int:
    # Convert the string into a list of [color, count] pairs
    lst = [[points[0], 1]]
    for p in points[1:]:
        if p == lst[-1][0]:
            lst[-1][1] += 1
        else:
            lst.append([p, 1])
    
    # Initialize the answer counter
    ans = 0
    
    # Perform operations until the list has only one element or less
    while len(lst) > 1:
        ans += 1
        tmp = []
        
        # Handle the first element
        if lst[0][1] > 1:
            tmp.append([lst[0][0], lst[0][1] - 1])
        
        # Handle the middle elements
        for i in lst[1:-1]:
            if i[1] > 2:
                if len(tmp) == 0 or tmp[-1][0] != i[0]:
                    tmp.append([i[0], i[1] - 2])
                else:
                    tmp[-1][1] += i[1] - 2
        
        # Handle the last element
        if lst[-1][1] > 1:
            if len(tmp) == 0 or lst[-1][0] != tmp[-1][0]:
                tmp.append([lst[-1][0], lst[-1][1] - 1])
            else:
                tmp[-1][1] += lst[-1][1] - 1
        
        # Update the list for the next iteration
        lst = tmp
    
    return ans