"""
QUESTION:
Write a function `find_nth(n)` that returns the Nth element in a sequence where each element is the sum of the previous three even numbers. If the sum is not even, append the last even number in the sequence plus 2 instead. The sequence starts with [0, 2, 4]. The function should handle positive integer inputs for N.
"""

def find_nth(n):
    l = [0, 2, 4] 
    i = 3
    while len(l) < n:
        temp = l[i-1] + l[i-2] + l[i-3]
        if temp % 2 == 0:
            l.append(temp)
        else:
            l.append(l[i-1] + 2)
        i += 1
    return l[n-1]