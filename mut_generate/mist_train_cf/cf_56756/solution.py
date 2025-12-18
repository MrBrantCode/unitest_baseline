"""
QUESTION:
Write a function `max_distance(X, Y)` that determines the time interval at which Cyclist X will be farthest from Cyclist Y, given their distances covered at various time intervals. The function should take two lists of tuples as input, where each tuple contains a time interval and the corresponding distance. The function should return a tuple containing the time interval with the maximum distance and the maximum distance itself.

The input lists X and Y are assumed to be sorted by time interval. The function should have a time complexity of O(n), where n is the maximum number of time intervals for either of the cyclists.
"""

def max_distance(X, Y):
    i = j = 0
    max_distance = 0
    max_interval = None

    while i < len(X) and j < len(Y):
        tX, dX = X[i]
        tY, eY = Y[j]
        
        diff = abs(dX - eY)
        if diff > max_distance:
            max_distance = diff
            max_interval = (tX, tY)     

        if dX < eY:
            i += 1
        else:
            j += 1

    return max_interval, max_distance